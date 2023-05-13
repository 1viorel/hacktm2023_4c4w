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
  cleanhist = {}

  for x in hist :
    if x.isalnum () :
      cleanhist [ x ] = hist [ x ]
  
  sorted_dict = sorted(cleanhist.items(), key=lambda x: -x[1])
  
  if ( len ( sorted_dict ) < rvi ) :
    rvi = len ( sorted_dict ) 
  print ( "SORT DICT PRINT" )
        
  return [pair[0] for pair in sorted_dict][:rvi]

# ~ with open('../response.json') as file:
  # ~ data = json.load(file)
  # ~ print ( ParseJsonResponseFromBing ( data ) )
