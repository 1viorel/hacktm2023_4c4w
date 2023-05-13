import json

def PrintKeys ( data ) :
  for x in data.keys () :
    print ( x ) 
    print ( data [ x ] ) 
    print ("-------------------------------")
  print ( data.keys () )

def GetSortedDict ( obj, hist ) :
  for y in obj :    
    for k in y [ 'name' ].split(" ") : 
      if k in hist :
        hist [ k ] += 1
      else :
        hist [ k ] = 1

def ParseJsonResponseFromBing ( data, rvi = 3 ) :   
  hist = {}
  
  GetSortedDict ( data ['tags'][0]['actions'][0]['data']['value'], hist )
  GetSortedDict ( data ['tags'][0]['actions'][2]['data']['value'], hist )

  sorted_dict = sorted(hist.items(), key=lambda x: -x[1])
  
  omega = []
  
  if ( len ( sorted_dict ) > rvi ) :
    rvi = len ( sorted_dict ) 
  
  print ( "SORT DICT PRINT" )
  print ( sorted_dict )
  
  for  i in range ( 0, rvi ) :
    omega.append ( sorted_dict [ i ] [ 0 ] )
        
  return omega
