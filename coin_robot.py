import random 
from draw import draw
import argparse
import numpy as np


class coin_robot:

    def __init__( self, row, column ):
        random.seed( 0 )
        self.row = row
        self.column = column 
        # Get map
        self.map = [ [ 0 for i in range( column ) ] for j in range( row )]
        self.generate_map()
        

        
    def generate_map(self):
        for i in range( self.row ):
            for j in range( self.column ):
                if random.random() > 0.7:
                    self.map[ i ][ j ] = 1 # coin
                else:
                    self.map[ i ][ j ] = 0

    def solve(self):
        #create a matrix self.row x self.column
        #populate our coin matrix with the correct coin locations
        # path = {}
        c = np.copy( self.map )
        parent={}
        F = [ [ 0 ] * ( self.column + 1 ) for i in range( self.row+1 ) ]
        for i in range( 1 , self.row + 1 ):
            for j in range( 1 , self.column + 1 ):
                parentIndex = i,j
                F[i][j] = max( F [ i - 1 ] [ j ] , F[ i ] [ j - 1 ] ) + c [ i - 1 ] [ j - 1 ] 
                if( F [ i ] [ j ] == F [ i - 1 ] [ j ] + c [ i - 1 ] [ j - 1 ]):
                    parent[ parentIndex ] = ( i - 1 , j )
                else:
                    parent[ parentIndex ] = ( i , j - 1 )

        #now backtrack to find the optimal path.
        child = self.row,self.column      
        path = []
        while 0 not in child:
            path.append( ( child[ 0 ] - 1 , child[ 1 ] - 1) )
            child = parent[ child ]
        self.draw( F [ -1 ][ -1 ], path )
        
        
        

        print( "matrix weghts" )
        print( np.matrix( F ) )
        print( "Max coins collected: " , F [ self.row -1 ] [ self.column - 1 ])

      

      
       
    def draw( self, F, path ):
        title = "row_" + str( self.row ) + "_column_" + str ( self.column ) + "_value_" +str( F )
        draw( self.map, path, title )

if __name__ == '__main__':

    parser = argparse.ArgumentParser( description= 'coin robot' )

    parser.add_argument( '-row' , dest='row' , required = True , type = int , help = 'number of row' )
    parser.add_argument( '-column', dest = 'column', required = True, type = int, help = 'number of column' )

    args = parser.parse_args()

    # Example: 
    # python coin_robot.py -row 20 -column 20
    game = coin_robot( args.row, args.column )
    game.solve()