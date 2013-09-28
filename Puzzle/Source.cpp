#include <iostream>
#include <string>

using namespace std;


int main()
{

}

/// version 1
void select_substring(const string &s, int p1, int p2) {
    // Write your code here
    // To print results to the standard output you can use the cout stream
    // Example: cout << "Hello world!";

	int len = s.length();
	if ( p1 >= len || p2  >= len ||  p1>p2 )
	{
		cout<<"Invalid pointers";
	}
	for(int i = p1-1 ; i <p2;i++)
	{
		cout<<s.at(i);
	}
    
}


/// version 2
void select_substring2(const string &s, int p1, int p2) {
    // Write your code here
    // To print results to the standard output you can use the cout stream
    // Example: cout << "Hello world!";

	int len = s.length();
	if ( p1 >= len || p2  >= len ||  p1>p2 )
	{
		cout<<"Invalid pointers";
	}
	cout<< s.substr(p1-1,p2);
    
}


void remove_substring(const string &s, int p, int n) {
    // Write your code here
    // To print results to the standard output you can use the cout stream
    // Example: cout << "Hello world!";

	if( p>=0 && n <= s.length()- p)
	{
		cout<<s.substr(0,p -1 ) << s.substr(p+n-1);
	}
    
}
