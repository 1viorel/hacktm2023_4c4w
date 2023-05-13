import json

def PrintKeys ( data ) :
  for x in data.keys () :
    print ( x ) 
    print ( data [ x ] ) 
    print ("-------------------------------")
  print ( data.keys () )

def GetSortedDict ( obj, rvi = 3 ) :
  hist = {}
  for y in obj :
    
    for k in y [ 'name' ].split(" ") : 
      if k in hist :
        hist [ k ] += 1
      else :
        hist [ k ] = 1

  sorted_dict = sorted(hist.items(), key=lambda x: -x[1])
  
  omega = []
  for  i in range ( 0, rvi ) :
    print ( sorted_dict [ i ] [ 0 ] )
    omega.append ( sorted_dict [ i ] [ 0 ] )
    
  return omega

with open('response.json') as file:
    data = json.load(file)

# ~ PrintKeys ( data )

# ~ PrintKeys ( data [ 'tags' ] [ 0 ] [ 'actions' ] [ 0 ] [ 'data' ] )

GetSortedDict ( data [ 'tags' ] [ 0 ] [ 'actions' ] [ 0 ] [ 'data' ] ['value'] )

# ~ PrintKeys ( data [ 'tags' ][ 0 ] )

# ~ print ( data [ 'tags' ] [ 0 ] [ 'actions' ] )

# ~ PrintKeys ( data [ 'tags' ] [ 0 ] [ 'actions' ] [ 0 ] [ 'data' ] ['value'][ 0 ] )

# ~ delta = data [ 'tags' ] [ 0 ] [ 'actions' ] [ 0 ] [ 'data' ] ['value'] 

# ~ print ( data [ 'tags' ] [ 0 ] [ 'displayName' ] )
# ~ PrintKeys ( data [ 'tags' ] [ 0 ] )
# ~ PrintKeys ( data [ 'tags' ] [ 1 ] )
# ~ PrintKeys ( data [ 'tags' ] [ 2 ] )
