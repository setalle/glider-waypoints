#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

"""wptool, a script to manipulate waypoint files in .cup (seeyou) format.

standard usage is "wptool.py command file1.cup [file2.cup]"
               or "python wptool.py command file1.cup [file2.cup]" 

NOTES: 
- THIS IS JUST A SCRIPT, USE AT YOUR OWN RISK
- waypoints file must be in the 2020 seeyou format
- it uses the library numpy and pandas

Author: "Sandro Etalle"
Version: 0.9 - 8/12/2020 """

# il robo non funziona se ci sono degli apici nei camp, del tipo "" a rompere le uova nel paniere
# 
#use python3 to handle this

#problema, quando faccio la lettura di seeyou2020 'style' e' un numero, quando faccio la lettura di Rieti2020 'style' e' una stringa,
#comunque se tolgo i task funziona
#
import numpy as np
import pandas as pd
import sys
import math
#import pdb; pdb.set_trace()

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def check_quotes(i,mystring):
    #this is used to check that something does not contains double quotes "
    if '"' in mystring:
        print('warning: at index ',str(i),' there is a string containing a quote namely ',mystring,' we have removed it')
    return(mystring.replace('"',''))

def clean_dataframe(df):
  """ testing the triple quotes """
  df=df.astype('str')
  #now we have to take away the 'nan'
  df.replace('nan','') # does not work, but I have kept it
  """ another test of the triple quotes"""
  #now we need to put the double quotes where needed, and remove the "nan"
  for i, wp in df.iterrows():
    df.at[i,'name'] = '"'+wp['name']+'"'
    if len(wp['code'])>8:
      print('record number {0} has a "code" whose length is greater than 8, which is non-compliant. The code is {1}'.format(i,wp['code']))
      # df.at[i,'code']= wp['code'][0:8]
    if wp['rwwidth']=='nan':
      df.at[i,'rwwidth'] = ''
    if wp['rwlen']=='nan':
      df.at[i,'rwlen'] = ''
    if wp['country']=='nan':
      df.at[i,'country'] = ''
    if wp['freq']=='nan':
      df.at[i,'freq'] = ''
    else:
      df.at[i,'freq']= '"'+check_quotes(i,wp['freq'])+'"'
    if wp['desc']!='nan':
      df.at[i,'desc'] = '"'+check_quotes(i,wp['desc'])+'"'
    else:
      df.at[i,'desc'] = ''
    if wp['userdata']!='nan':
      df.at[i,'userdata'] = '"'+check_quotes(i,wp['userdata'])+'"'
    else:
      df.at[i,'userdata'] = ''
    if wp['pics']!='nan':
      df.at[i,'pics'] = '"'+check_quotes(i,wp['pics'])+'"'
    else:
      df.at[i,'pics'] = ''
    #now I kill the line with "related tasks"
    if "Related Tasks" in wp['name']:
      df=df.drop([i])
      print('dropped one line')
  return(df)

def add_prefix_to_name(df,mystring):
  for i, wp in df.iterrows():
      df.at[i,'name'] = '"'+mystring+wp['name'][1:]
  return(df)

def add_suffix_to_name(df,mystring):
  for i, wp in df.iterrows():
      df.at[i,'name'] = wp['name'][0:-1]+mystring+'"'
  return(df)

def add_string_to_desc(df,mystring):
    for i, wp in df.iterrows():
        if wp['desc'] in ['nan','']:
            df.at[i,'desc'] = '"'+mystring+'"'
        else:
            df.at[i,'desc'] = wp['desc'][0:-1]+' '+mystring+'"'
    return(df)

def out_nan(f,mystr):
    if mystr!='nan':
        n = f.write(mystr)

def print_compare(wp1,wp2):
  for arg in ['name','code','country','lat','lon','elev','style','rwdir','rwlen','rwwidth','freq','desc','userdata','pics']:
    print('{0:<9}:{1:<35}:{2:<35}'.format(arg,wp1[arg][0:32],wp2[arg][0:32]))
  #I would like this to work by just pressing the character, but python does not suppor this  
  choice=input("\nNow make a choice: 1 = remove left, 2 = remove right, anything else = keep both:\n")
  try:
    a=int(choice)
  except ValueError:
    a=0
  print("choice =",a,'\n')
  return(a)
        
def write_dataframe(df,filename):
    f = open(filename, "x")
    n = f.write('name,code,country,lat,lon,elev,style,rwdir,rwlen,rwwidth,freq,desc,userdata,pics\n')
    for i, wp in df.iterrows():
        n = f.write(wp['name']+','+wp['code']+','+wp['country']+','+wp['lat']+','+wp['lon']+','+wp['elev']+','+wp['style'])
        n = f.write(','+wp['rwdir']+','+wp['rwlen']+','+wp['rwwidth']+','+wp['freq']+','+wp['desc']+','+wp['userdata']+','+wp['pics'])
        n = f.write('\n')
    n=f.write('-----Related Tasks-----\n')
    f.close

def remove_from_dataframe(df1,file1,removefrom1):
  newfilename=file1[0:-4]+'_trimmed.cup'
  write_dataframe(df1.drop(removefrom1),newfilename)
  
#convert the N coordinates into DD
def n_conv(mystr):
    return float(mystr[0:2])+(float(mystr[2:8])/60)

def e_conv(mystr):
    return float(mystr[0:3])+(float(mystr[3:9])/60)
    
#this distance is more or less in km, assuming a latitude of about 45 degrees
def distance(wp1,wp2):
  dns = n_conv(wp1['lat'])-n_conv(wp2['lat'])
  dew = e_conv(wp1['lon'])-e_conv(wp2['lon'])
  return math.sqrt((dns*dns)*12321+(dew*dew)*8712)

def split_datagram(df,filename):
  #splits a file.cup and returns four files: file_landables.cup, file_airfields.cup, file_outlandings.cup, file_nonlandables.cup
  newfilename=filename[0:-4]+'_landables.cup'
  df1 = df.query('style in ["2","3","4","5"]')
  write_dataframe(df1,newfilename)
  newfilename=filename[0:-4]+'_airfields.cup'
  df1 = df.query('style in ["2","4","5"]')
  write_dataframe(df1,newfilename)
  newfilename=filename[0:-4]+'_outlandings.cup'
  df1 = df.query('style in ["3"]')
  write_dataframe(df1,newfilename)
  newfilename=filename[0:-4]+'_nonlandables.cup'
  df1 = df.query('style not in ["2","3","4","5"]')
  write_dataframe(df1,newfilename)


def split():
  """ =============
  command: split
  usage: work.py split file.cup 
 
  it produces four subfiles of 'file' called: file_landables.cup, file_airfields.cup, file_outlandings.cup, file_nonlandables.cup
  notice that file_landables.cup = file_airfields.cup + file_outlandings.cup 
  and that    file.cup = file_landables.cup + file_nonlandables.cup """
  print('inside split now')
  file1=sys.argv[2]
  df1 = pd.read_csv(file1, dtype=str) 
  df1 = clean_dataframe(df1) #here dtype=string should convert everything to string, but it does not, so we do the trimming
  split_datagram(df1,file1)
  quit()


def check():
  """ =============
  command: check
  usage: work.py check file.cup 

  this is used to check that a file does not contains double quotes "" somewhere, that would indicate a mistake, and mess up the python scripts
  the output of this command is written in the file 'test.cup', the original file is left unaltered
  test.up has no double quotes, and the field 'code' is truncated to the first 8 characters
  
  the command also gives a warning when there is a wp that ha a 'code' whose length exceeds 8 characters, 
  which is something that seeyou does not allow. The 'code' field is not changed, it just gives the warning """
  file1=sys.argv[2]
  #load dataframe from csv
  #here dtype=string should convert everything to string, but it does not, so we do the trimming
  df1 = pd.read_csv(file1, dtype=str)
  df1 = clean_dataframe(df1)
  print('the result of the cleaning will be stored in the file test.cup (provided it is not already present)\n')
  print('the original file will stay unchanged \n')
  df1 = write_dataframe(df1,'test.cup')


def diff_compare(task):
    file1=sys.argv[2]
    file2=sys.argv[3]
    #load dataframe from csv
    #here dtype=string should convert everything to string, but it does not, so we do the trimming
    df1 = pd.read_csv(file1, dtype=str)
    df1 = clean_dataframe(df1)
    df2 = pd.read_csv(file2, dtype=str) 
    df2 = clean_dataframe(df2)
    #filtering out everything that is non-landable
    df1 = df1.query('style in ["2","3","4","5"]')
    df2 = df2.query('style in ["2","3","4","5"]')
    removefrom1 = []
    removefrom2 = []
    solitarywps = []
    for i1, wp1 in df1.iterrows():
        a = 0
        for i2, wp2 in df2.iterrows():
            if distance(wp1,wp2)<3:
                print(wp1['name'],wp2['name'],str(distance(wp1,wp2)))
                if task=='compare':
                     choice = print_compare(wp1,wp2)
                     if choice==1:
                       removefrom1.append(i1)
                     elif choice==2:
                       removefrom2.append(i2)
                a = a+1
        if a==0: solitarywps.append(wp1['name'])
    if task=='compare':
      remove_from_dataframe(df1,file1,removefrom1)
      remove_from_dataframe(df2,file2,removefrom2)
    else:
      print('\nLandables in the first file having no match in the second file are:')
      print(solitarywps)
      

def diff_compare_self():
    print('TEST')
    file1=sys.argv[2]
    #file2=sys.argv[3]
    #load dataframe from csv
    #here dtype=string should convert everything to string, but it does not, so we do the trimming
    df1 = pd.read_csv(file1, dtype=str)
    df1 = clean_dataframe(df1)
    #df2 = pd.read_csv(file2, dtype=str)
    #df2 = clean_dataframe(df2)
    #filtering out everything that is non-landable
    df1 = df1.query('style in ["2","3","4","5"]')
    #df2 = df2.query('style in ["2","3","4","5"]')
    removefrom1 = []
    #removefrom2 = []
    solitarywps = []
    for i1, wp1 in df1.iterrows():
        a = 0
        for i2, wp2 in df1.iterrows():
            if i2>i1:
                if distance(wp1,wp2)<3:
                    print(wp1['name'],wp2['name'],str(distance(wp1,wp2)))
                    choice = print_compare(wp1,wp2)
                    if choice==1:
                       removefrom1.append(i1)
                    elif choice==2:
                       removefrom1.append(i2)
    print('\nProcedure check_duplicates finished\n')
    remove_from_dataframe(df1,file1,removefrom1)

def diff():
  """ ==============
  command:  diff
  usage:    work.py diff file1.cup file2.cup

  diff: does 2 things
  (a) for each landable wp1 in file1 shows if there is a landable wp2 in file2 at less than 6 km, indicating the names and the distance
  (b) lists all the wp in file1 who have no "close" (at less than 6 km) wp in file 2 """
  diff_compare('diff')

def compare():
  """ ================
  command: compare
  usage: work.py compare file1.cup file2.cup

  "compare" is the extended version of diff and allows to remove 
  the colliding waypoints from one file or the other 

  for each wp1 in file1 and wp2 in file2 it shows the records next to each 
  other together with the distance separating them, and allows to
  choose to remove wp1 from file1 or wp2 from file2 or leave them both
  the results are then stored in the files file1_trimmed.cup and file2_trimmed.cup
  the originals file1.cup and file2.cup are left unchanged """
  diff_compare('compare')


def check_duplicates():
  """ ================
  command: check_duplicates
  usage: work.py check_duplicates file1.cup

  like "compare" but checking with the same file and excluding the obvious duplicates (that is, fields with the same name)"""

  diff_compare_self()


def addprefixtoname():
  """ ==============
  command:  addprefixtoname
  usage:    work.py addprefixtoname mystr file1.cup 

  the string "mystr" is added as prefix to the record 'name' to each waypoint in  file.cup
  the result is stored in file1_withprefix.cup
  this is useful to modify the labels of a whole file before merging it with another one
  this way one can compare two wp files using seeyou, being able to distinguish which wp comes from which file
  the prefix can be then removed with a function delprefix (TBD)"""
  mystring=sys.argv[2]
  file1=sys.argv[3]
  df1 = pd.read_csv(file1, dtype=str)
  df1 = clean_dataframe(df1)
  df1 = add_prefix_to_name(df1,mystring)
  newfilename=file1[0:-4]+'_withprefix.cup'
  write_dataframe(df1,newfilename)

def addsuffixtoname():
  """  ==============
  command:  addsuffixtoname
  usage:    work.py addsuffixtoname mystr file1.cup 

  like addprefixtoname but the string mystr is appended to the 'name' field of each waypoint in file1
  the result is stored in the file file1_withsuffix.cup """
  mystring=sys.argv[2]
  file1=sys.argv[3]
  df1 = pd.read_csv(file1, dtype=str)
  df1 = clean_dataframe(df1)
  df1 = add_suffix_to_name(df1,mystring)
  newfilename=file1[0:-4]+'_withsuffix.cup'
  write_dataframe(df1,newfilename)


def addsuffixtodesc():
  """  ==============
  command: addsuffixtodesc 
  usage:   work.py addsuffixtodesc mystr file1.cup 

  like addsuffixtoname but the string mystr is appended to the 'description' field of each waypoint in file1
  the result is stored in the file file1_withsuffix.cup 
  this can be useful to label "internally" the waypoints in a file, I use it to put in the record the source of the waypoint"""
  
  mystring=sys.argv[2]
  file1=sys.argv[3]
  df1 = pd.read_csv(file1, dtype=str)
  df1 = clean_dataframe(df1)
  df1 = add_string_to_desc(df1,mystring)
  newfilename=file1[0:-4]+'_withsuffix.cup'
  write_dataframe(df1,newfilename)



##########################################################
# HERE WE START
##########################################################
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

listofcommands=['split', 'diff', 'compare', 'check_duplicates', 'check', 'addprefixtoname', 'addsuffixtoname', 'addsuffixtodesc']

if len(sys.argv)==1:
  # no arguments are passed, so the command is non-existent, in this case we show the help
  print(__doc__)
  for possible_task in listofcommands:
    print(eval(possible_task).__doc__)
  quit()

command=sys.argv[1]

if command in listofcommands:
  # now the case in which the first argument is a recognized command
  # for each allowed command cmd, we have defined the function cmd()
  # we use this trick to call it directly
  # the trick would be dangerous had we not checked that the command is legitimate
  fullcommand = command+'()'
  eval(fullcommand)
  quit()
else:
  # now the case in which the first argument is a not a recognized command
  # we say so and we print the help
  print('\nERROR:',command,' is not a recognized command\n')
  print('recognized commands are ',listofcommands) 
  print(__doc__)
  for possible_command in listofcommands:
    print(eval(possible_command).__doc__)
  quit()


