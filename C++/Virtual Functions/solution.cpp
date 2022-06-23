#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class Person {
protected:
    int m_id;
    std::string m_name;
    int m_age;
public:
    virtual ~Person() = default;
    
    virtual void getdata() {
        cin >> m_name;
        cin >> m_age;
    }
    virtual void putdata() {
        cout << m_name << " " << m_age;
    }
};

class Professor : public Person {
private:
    static int createid() {
        static int id = 0;
        return ++id;
    }

    int m_publications;
public:
    void getdata() override {
        Person::getdata();
        cin >> m_publications;
        m_id = createid();
    }
    
    void putdata() override {
        Person::putdata();
        cout << " " << m_publications << " " << m_id << endl;
    }
};

class Student : public Person {
private:
    static int createid() {
        static int id = 0;
        return ++id;
    }

    int m_remarks[6];
public:
    void getdata() override {
        Person::getdata();
        for (int i = 0; i < 6; ++i) {
            cin >> m_remarks[i];
        }
        m_id = createid();
    }
    
    void putdata() override {
        Person::putdata();
        int sum = 0;
        for (int i = 0; i < 6; ++i) {
            sum += m_remarks[i];
        }
        cout << " " << sum << " " << m_id << endl;
    }
};

int main(){

    int n, val;
    cin>>n; //The number of objects that is going to be created.
    Person *per[n];

    for(int i = 0;i < n;i++){

        cin>>val;
        if(val == 1){
            // If val is 1 current object is of type Professor
            per[i] = new Professor;

        }
        else per[i] = new Student; // Else the current object is of type Student

        per[i]->getdata(); // Get the data from the user.

    }

    for(int i=0;i<n;i++)
        per[i]->putdata(); // Print the required output for each object.

    return 0;

}
