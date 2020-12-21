#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int main (int argc, char *argv[]){
  // Check input argument
  if (argc != 2) {
	  cout << "[main.c] Argumento Inválido" << endl;
    return 0;
  }
  
  // Show argument
  string file = argv[1];
  cout << "File: " << file << endl; 



  ifstream ffile (file);
  string line;
  vector <char> vetor;

  int x = 0;
  if (ffile.is_open()) {
 	while (getline(ffile, line)) {
		for (int i = 0; i < line.size(); i++) {
			vetor.push_back(line[i]);
		}
	}


	ffile.close();
  }

  vetor.push_back(-1); // set EOF
  
  for (int i = 0; i < vetor.size(); i++) { cout <<  vetor[i] << endl; }


  return 0;
}
