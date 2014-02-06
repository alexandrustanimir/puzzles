#include <iostream>
#include <vector>
#include <stack>
#include <map>
using namespace std;

struct PlaneTicket
{
	PlaneTicket* Previous;
	int destination;
	int departure;
	PlaneTicket* Next;
	void AddPrevious(PlaneTicket* p)
	{
		Previous = p;
	}
	void AddNext(PlaneTicket* p)
	{
		Next = p;
	}
	bool ContainsValue(int value)
	{

	}
};

void get_journey(const vector<int> &departure_ids, const vector<int> &destination_ids) {
	// Write your code here
	// To print results to the standard output you can use the cout stream
	// Example: cout << "Hello world!";

	PlaneTicket journey;
	journey.Previous = NULL;
	journey.Next = NULL;
	journey.destination = destination_ids.at(0);

	PlaneTicket begin;
	begin.Previous = NULL;
	map<int, int> flights;


	for (int i = 0; i < departure_ids.size(); i++)
	{
	bool	found = false;
		for (int j = 0; j < destination_ids.size(); j++)
		{
			if (i == j)continue;
			if (departure_ids.at(i) == destination_ids.at(j))
			{
				found = true;
				j = destination_ids.size();
			}
		}
		if (!found){
			begin.departure = departure_ids.at(i);
			begin.destination = destination_ids.at(i);
			i = departure_ids.size();
		}
	}
	
	int count = 0;
	for (int i = 0; i < destination_ids.size(); i++)
	{
		pair<int, int>
			*value = new pair<int, int>(departure_ids.at(i), destination_ids.at(i));
		flights.insert(*value);
	}
	
	while (count < destination_ids.size()-1)
	{
		
				cout << begin.departure;
				cout << " ";
				begin.departure = begin.destination;
				begin.destination = flights.at(begin.departure);
				count++;
	}
	cout << begin.departure;
	cout << " ";
	cout << begin.destination;

}

int main()
{
	vector<int>  dep = {0,1};
	vector<int>  dest = {2,0};
	get_journey(dep, dest);

}