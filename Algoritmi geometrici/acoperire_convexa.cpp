#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

bool viraj_stanga(long long px, long long py,long long qx, long long qy, long long rx, long long ry){
    long long d = (px - rx) * (qy - ry) - (py - ry) * (qx - rx);
    return d > 0;
}

bool cmp(pair<long long, long long> a, pair<long long, long long> b){
    if(a.first != b.first){
        return a.first < b.first;
    }else{
        return a.second < b.second;
    }
}

bool cmp_rev(pair<long long, long long> a, pair<long long, long long> b){
    if(a.first != b.first){
        return a.first > b.first;
    }else{
        return a.second > b.second;
    }
}


int main()
{
    long long n;
    cin>>n;
    vector<pair<long long, long long>> lista;

    for(long long i=0; i<n; i++){
        long long a, b;
        cin>>a>>b;
        lista.push_back(make_pair(a, b));
    }

    sort(lista.begin(), lista.end(), cmp);

    vector<pair<long long, long long>> acoperire;
    acoperire.push_back(lista[0]);
    acoperire.push_back(lista[1]);

    for(long long i=2; i<n;i++){
        acoperire.push_back(lista[i]);
        long long x = acoperire.size();

        if(!viraj_stanga(acoperire[x-3].first, acoperire[x-3].second, acoperire[x-2].first, acoperire[x-2].second, acoperire[x-1].first, acoperire[x-1].second))
        {
            acoperire.erase(acoperire.begin() + x-2);
            x = acoperire.size();
            while(x > 2 && !(viraj_stanga(acoperire[x-3].first, acoperire[x-3].second, acoperire[x-2].first, acoperire[x-2].second, acoperire[x-1].first, acoperire[x-1].second)))
            {
                acoperire.erase(acoperire.begin() + x-2);
                x = acoperire.size();
            }
        }
    }


    sort(lista.begin(), lista.end(), cmp_rev);

    vector<pair<long long, long long>> acoperire2;
    acoperire2.push_back(lista[0]);
    acoperire2.push_back(lista[1]);

    for(long long i=2; i<n;i++){
        acoperire2.push_back(lista[i]);
        long long x = acoperire2.size();

        if(!viraj_stanga(acoperire2[x-3].first, acoperire2[x-3].second, acoperire2[x-2].first, acoperire2[x-2].second, acoperire2[x-1].first, acoperire2[x-1].second))
        {
            acoperire2.erase(acoperire2.begin() + x-2);
            x = acoperire2.size();
            while(x > 2 && !(viraj_stanga(acoperire2[x-3].first, acoperire2[x-3].second, acoperire2[x-2].first, acoperire2[x-2].second, acoperire2[x-1].first, acoperire2[x-1].second)))
            {
                acoperire2.erase(acoperire2.begin() + x-2);
                x = acoperire2.size();
            }
        }

    }


    for(long long i=0; i<acoperire2.size(); i++)
    {
        if(find(acoperire.begin(), acoperire.end(), acoperire2[i]) == acoperire.end())
        {
            acoperire.push_back(acoperire2[i]);
        }

    }

    cout<<acoperire.size()<<endl;
    for(long long i=0; i<acoperire.size(); i++)
    {
        cout<<acoperire[i].first<<" "<<acoperire[i].second<<endl;
    }



    return 0;
}






