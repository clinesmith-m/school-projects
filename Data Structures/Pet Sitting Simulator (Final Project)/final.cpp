#include <iostream>
#include <vector>
#include "Pet.h"
#include "Client.h"
using namespace std;

// Filling a vector of pet names.
void fillPetNames(vector<string>* names) {
  names->push_back("Fido");
  names->push_back("Buddy");
  names->push_back("Biscuit");
  names->push_back("Carter");
  names->push_back("Daisy");
  names->push_back("Fritz");
  names->push_back("Keanu");
  names->push_back("Max");
  names->push_back("Moses");
  names->push_back("Dash");
  names->push_back(".size()");
  names->push_back("Lenny");
  names->push_back("Phyllis");
  names->push_back("Studebaker");
  names->push_back("Charlie");
  names->push_back("Snacks");
  names->push_back("Rocky");
  names->push_back("Augustus");
  names->push_back("Cat");
  names->push_back("Dog");
  names->push_back("Parrot");
  names->push_back("Frankie");
  names->push_back("Buffie");
  names->push_back("Fin");
}


int main() {

  srand(time(NULL));
  
  // Making a vector to hold pet names.
  vector<string> petNames;
  fillPetNames(&petNames);

  // Making a vector of Clients to iterate through when playing.
  vector<Client*> clients;
  Client* c1 = new Client ("Cher", petNames);
  clients.push_back(c1);

  Client* c2 = new Client ("Madonna", petNames);
  clients.push_back(c2);

  Client* c3 = new Client ("Tom Cruise", petNames);
  clients.push_back(c3);

  Client* c4 = new Client ("Arthur, King of the Britains", petNames);
  clients.push_back(c4);

  Client* c5 = new Client ("Lenny Somebody", petNames);
  clients.push_back(c5);

  // Explaining game mechanics to the player.
  cout << "You haved been hired for a summer job as a pet caretake... " << endl;
  cout << "TO THE STARS! ... (mostly.)." << endl;
  cout << "Your job: feed, water, pet, walk, and appease their pets as necessary." << endl;
  cout << "Just type 'command petname' to get your work done." << endl;

  // Letting the player determine how long they wish to play for.
  int finishValue;
  cout << "Now, how much money do you wish to make?" << endl;
  cin >> finishValue;
  cin.ignore();
  cout << "Great! Now let's get started!" << endl;

  // Initalizing a variable to track the player's cash.
  int playerCash = 0;

  // Creating a game loop.
  while (playerCash < finishValue) {
    // And a loop to iterate through the clients vector.
    for (int i = 0; i < clients.size(); i++) {
      cout << clients[i]->getName() << "'s pet(s) are feeling thusly:" << endl;
      clients[i]->showPetNeeds();
      // And a loop to give the player three moves per client.
      for (int turn = 0; turn < 3; turn++) {
        cout << "What will you do?" << endl;
        string command;
        getline(cin, command);
        playerCash += clients[i]->processInput(command);
      }
      cout << clients[i]->getName() << " is satisfied with your efforts." << endl;
      cout << "You now have $" << playerCash << "." << endl;
      // Incrementing the needs for the client's pets.
      clients[i]->runPetIncrements();
    }
    
  }

 cout << "You win! Yay!" << endl; 
  
  return 0;
}
