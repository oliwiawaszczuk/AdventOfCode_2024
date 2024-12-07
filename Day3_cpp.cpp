#include <iostream>
#include <fstream>
#include <string>
#include <chrono>

using namespace std;
using namespace chrono;


struct str {
    string whole_str;
    str *next;
    str() : next(nullptr) {}
};


struct stos {
    str *first;
    int count;

    stos() : first(nullptr), count(0) {}

    void add(const string &new_str) {
        str *new_s = new str;
        new_s->whole_str = new_str;
        new_s->next = nullptr;

        if (count == 0) first = new_s;
        else {
            str *curr = first;
            while (curr->next != nullptr)
                curr = curr->next;

            curr->next = new_s;
        }

        count++;
    }

    void remove(int how_many) {
        for (int i = 0; i < how_many; i++) {
            if (first != nullptr) {
                str *temp = first;
                first = first->next;
                delete temp;
                count--;
            } else {
                cout << "Stos jest pusty, nie można zdjąć elementu." << endl;
                break;
            }
        }
    }

    int size() const {
        return count;
    }

    void print() const {
        cout << "String: ";
        for (str *current = first; current != nullptr; current = current->next)
            cout << current->whole_str;
        cout << endl;
    }

    bool is_next(string what_next) {
        if (what_next.length() > size()) return false;
        str *current = first;
        string temp_str = "";
        for(int i=0; i<what_next.length(); i++) {
            temp_str += current->whole_str;
            current = current->next;
        }
        return temp_str == what_next ? true : false;
    }

    string get_number() {
        string number = "";
        for (str *current = first; current != nullptr; current = current->next)
            if (current->whole_str >= "0" && current->whole_str <= "9")
                number += current->whole_str;
            else break;
        remove(number.length());
        return number;
    }
};

int main() {
    auto start = high_resolution_clock::now();
    stos stos_whole_str;

    // FILE READING
    string line = "";
    string lines_reader = "";
    ifstream file("R:\\PROGRAMOWANIE\\PYTHON\\AdventOfCode\\data\\Day3_file.txt");
    while(getline(file, lines_reader))
        line += lines_reader;
    file.close();

    for(int i = 0; i < line.size(); i++) {
        string single_char(1, line[i]);
        stos_whole_str.add(single_char);
    }

    bool is_mul = true;
    string number1 = "", number2 = "";
    int suma = 0;

    stos_whole_str.print();
    cout << "size: " << stos_whole_str.size() << endl;
    while (stos_whole_str.size() > 6) {
        while (stos_whole_str.size() > 0 && !stos_whole_str.is_next("mul(")) { // looking for mul( start
            bool is_do = stos_whole_str.is_next("do()");
            if (is_do) is_mul = true;

            bool is_do_not = stos_whole_str.is_next("don't()");
            if (is_do_not) is_mul = false;

            stos_whole_str.remove(1);
        }
        if (stos_whole_str.size() <= 4) break;

        stos_whole_str.remove(4); // removing mul(
        number1 = stos_whole_str.get_number();
        if (number1 != "" && stos_whole_str.is_next(",")) {
            stos_whole_str.remove(1);
            number2 = stos_whole_str.get_number();
            if (number2 != "" && stos_whole_str.is_next(")")) {
              // everytring good - count multipy
              stos_whole_str.remove(1);
              if (is_mul)
                  suma += stoi(number1) * stoi(number2);
            }
        } else number1 = "";
//        stos_whole_str.print();
    }

    cout << "Total sum: " << suma << endl;

    auto end = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(end - start);
    cout << "Execution time: " << duration.count() << " ms" << endl;
    return 0;
}