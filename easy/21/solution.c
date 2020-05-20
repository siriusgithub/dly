int next_perm( char *symbols ) {
    char *s, *t, *p = symbols ;
    if( !p || !*p ) return 0 ;  
    while( *p ) ++p ;                        // move p to trailing \0
    t = --p ;                                // mark last char
    while( p!=symbols && *(p-1)>=*p ) --p ;  // walk backwards up hill
    if( p==symbols ) return 0 ;              // all hill? no next perm
    for( s=t,--p ; *p>=*s ; --s ) ;          // from tail, find level higher than dip
    SWAP( p, s ) ;                           // lift dip
    while( ++p<t ) {
        SWAP( p, t ) ; --t ;                 // reverse hill slope
        }
    return 1 ;
    }  

( obvious #define SWAP() )  