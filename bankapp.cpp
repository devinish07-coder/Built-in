#include<iostream>
using namespace std;
class bankaccount{
    string name;
    float balance;
    public:
    bankaccount(string n, float b)
    {
        name=n;
        balance=b;
    }
    void deposit(float amt){
        balance +=amt;
        cout<<"amount depaosited"<<amt<<endl;
    }
    void withdraw(float amt){
        if(amt>balance)
        cout<<"insufficient balance!"<<endl;
        else{
            balance-=amt;
            cout<<"amount withdrawn:"<<amt<<endl;
        }
    }
    void display()
    {
        cout<<"customer:"<<name<<endl;
        cout<<"balance:"<<balance<<endl;
    }
};
int main()
{
    bankaccount acc("priya",1000);
    acc.deposit(1000);
    acc.withdrawn(500);
    acc.display();
    return 0;
}