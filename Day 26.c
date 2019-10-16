#include <stdio.h>

int main() {

    int ad,am,ay,ed,em,ey,fine=0;
    scanf("%d %d %d",&ad,&am,&ay);
    scanf("%d %d %d",&ed,&em,&ey);
    if(ad==ed)
    {
        fine=0;
    }
    if(ad>ed && am==em && ay==ey)
    {
        fine=fine+15*(ad-ed);
    }
    if(am>em && ay==ey)
    {
        fine=fine+500*(am-em);
    }
    if(ay>ey)
    {
        fine=10000;
    }
    printf("%d",fine);

    return 0;
}
