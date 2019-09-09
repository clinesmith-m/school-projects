#ifndef CLIENT_H
#define CLIENT_H

#include <iostream>
#include <vector>
#include <time.h>
#include <algorithm>
#include <sstream>
#include "Pet.h"
using namespace std;

class Client {
  private:
    // I'm giving every client a vector of pets, just as
    // a basic way of organizing the game,
    vector<Pet*> pets;

    // The petNames vector allows for somewaht distinct random pet names.
    vector<string> petNames;

    // Whatever money a player earns from a task will be multiplied
    // by the baller factor of the client who owns it.
    int ballerFactor;

    // Every client needs a name.
    string name;

    // Rather than sending pet objects to the client
    // I'm having the client generate it's own vector of
    // 1-5 pets.
    void generatePets(vector<string> petNames) {
      int index;
      string currName;
      // Creating a for loop that runs 1-5 times.
      for (int i = 0; i < (rand() % 3) + 1; i++) {
        // Grabs a random name from petNames.
        index = (rand() % petNames.size());
        currName = petNames[index];

        // Creating pet objects, using the value of i
        // to determine which constructor is called.
        if (i == 0) {
          Pet* pet0 = new Cat (currName);
          pet0->runIncrements();
          pets.push_back(pet0);
        } else if (i == 1) {
          Pet* pet1 = new Dog (currName);
          pet1->runIncrements();
          pets.push_back(pet1);
        } else if (i == 2) {
          Pet* pet2 = new Parrot (currName);
          pet2->runIncrements();
          pets.push_back(pet2);
        } else if (i == 3) {
          Pet* pet3 = new Cat (currName);
          pet3->runIncrements();
          pets.push_back(pet3);
        } else {
          Pet* pet4 = new Dog (currName);
          pet4->runIncrements();
          pets.push_back(pet4);
        }
      }

      // Shuffling the pets vector so that it appears that
      // it's been constructed more randomly.
      random_shuffle(pets.begin(), pets.end());
    }

  public:
    Client(string clientName, vector<string> possiblePetNames) {
      name = clientName;
      // Creating a random ballerFactor between 1-5.
      ballerFactor = (rand() % 4) + 1;
      petNames = possiblePetNames;
      generatePets(petNames);
    }



    // Iterating through every pet in the pets vector and calling its
    // showNeeds function.
    void showPetNeeds() {
      for (int i = 0; i < pets.size(); i++) {
        pets[i]->showNeeds();
      }
    }



    // Iterating through every pet in the pets vector and calling
    // its runIncrements function.
    void runPetIncrements() {
      for (int i = 0; i < pets.size(); i++) {
        pets[i]->runIncrements();
      }
    }



    // Processing player commands and running corresponding functions.
    int processInput(string playerInput) {
      // Creating a variable to track how much the player makes this turn.
      int cashMade = 0;

      // Splitting the input into the pet's name
      // and the command.
      string command = "";
      string petName = "";
      int space = playerInput.find(" ", 0);
      if (space != -1) {
        petName = playerInput.substr(space + 1);
        command = playerInput.substr(0, space);
      }

      // Appeasing the parrot is a special case, so I take care of that here.
      if (command == "appease") {
        cashMade += appeaseParrot(petName);
        return cashMade;
      }

      // Handling normal cases.
      for (int i = 0; i < pets.size(); i++) {
        // If a pet's name is equal to the name of one of the client's
        // pets, check to see what the command is.
        if (petName == pets[i]->getName()) {
          // Each if statement checks to see whether the command
          // is valid.
          if (command == "feed") {
            cashMade += pets[i]->feed();
            cout << "Success!" << endl;
          } else if (command == "water") {
            cashMade += pets[i]->water();
            cout << "Success!" << endl;
          } else if (command == "pet") {
            cashMade += pets[i]->pet();
            cout << "Success!" << endl;
          // This if statement also checks to make sure that the pet
          // is a dog before I try to walk it.
          } else if (command == "walk" && pets[i]->getSpecies() == "dog") {
            cashMade += pets[i]->special();
            cout << "Success!" << endl;
          }
        }
      }
      // Alerting the player that their command didn't work
      // if the player made no money.
      if (cashMade == 0) {
        cout << "Invalid command. " << name 
          << " is not pleased. Lose one turn." << endl;
      }
      // Returning whatever the player made, times the client's ballerFactor.
      return cashMade*ballerFactor;
    }



    int appeaseParrot(string nameAmount) {
      // Creating a return value.
      int cashLost = 0;

      int space = nameAmount.find(" ", 0);

      // Using stringstream to convert the player's input to an int.
      int amount;
      string tmpAmount = nameAmount.substr(space);
      stringstream ssAmount(tmpAmount);
      ssAmount >> amount;

      // Getting the pet's name and iterating through pets to look for it.
      string petName = nameAmount.substr(0, space);
      for (int i = 0; i < pets.size(); i++) {
        if (petName == pets[i]->getName() && pets[i]->getSpecies() == "parrot") {
          // Running appease and returning cashLost.
          cashLost += pets[i]->special(amount);
          cout << "Success!" << endl;
          return cashLost;
        }
      }

      // Alerting the player that their command didn't work.
      cout << "Invalid command. " << name 
        << " is not pleased. Lose one turn." << endl;
      // Returning 0 if no parrot is found.
      return 0;
    }

    // Grabbing the client's name.
    string getName() {
      return name;
    }
};

#endif
