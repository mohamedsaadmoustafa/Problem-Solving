def DesignerDoorMat( n, m ):
    range_ = range( 1, n, 2 )
    for i in range_:
        print( ( '.|.' * i ).center( m, '-' ) )
    
    print( 'WELCOME'.center( m, '-' ) )

    for i in range_[::-1]:
        print( ( '.|.' * i ).center( m, '-' ) )

n, m = map(int, input().split())
DesignerDoorMat( n, m )
