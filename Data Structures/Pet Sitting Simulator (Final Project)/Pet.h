#ifndef PET_H
#define PET_H

#include <iostream>
#include <time.h>
#include <stdlib.h>
using namespace std;

class Pet {
  private:
    // Increasing the animal's various needs.
    void incHunger() {
      int incValue = (rand() % hungerMax);
      hunger += incValue;
    }
    void incThirst() {
      int incValue = (rand() % thirstMax);
      thirst += incValue;
    }
    void incNeediness() {
      int incValue = (rand() % needinessMax);
      neediness += incValue;
    }

  protected:
    // These'll be the basic needs that the player has to monitor.
    int hunger;
    int thirst;
    int neediness;

    // Maximum amount any attribute can increase in a given round.
    int hungerMax;
    int thirstMax;
    int needinessMax;

    // The pet's name.
    string name;
  public:

    // Very basic constructor.
    Pet(string petName) {
      name = petName;
      hunger = 0;
      thirst = 0;
      neediness = 0;
    }

    // Calls each need attribute's individual increment function. 
    virtual void runIncrements() {
      incHunger();
      incThirst();
      incNeediness();
    }

    // Prints out a given animal's needs.
    virtual void showNeeds() = 0;

    // These functions set need attributes to zero and 
    // return the amount of money that the player earns.
    int feed() {
      hunger = 0;
      return 8;
    }
    int water() {
      thirst = 0;
      return 4;
    }
    int pet() {
      neediness = 0;
      return 5;
    }
    // Creating an optional special function that can take care of
    // any additional needs that species has.
    virtual int special(int inValue=0) = 0;

    // Creating a function that will return a string
    // representation of the animal's species. This
    // will allow for conditional logic, as well as
    // error handling.
    virtual string getSpecies() = 0;

    // Returns the name of the pet.
    string getName() {
      return name;
    }
};



class Cat : public Pet {
  private:

  public:
    // Constructor sets max amount that an attribute 
    // can increase in a given turn.
    Cat(string catName) : Pet(catName) {
      hungerMax = 3;
      thirstMax = 2;
      needinessMax = 10;
    }

    void speak() { cout << "Meow." << endl; }
    int special(int inValue=0) { 
      return 0; 
    }

    // Prints out the values of need attributes
    // rather than returning them.
    void showNeeds() {
      cout << name << " the cat needs: food(" << hunger
        << "), water(" << thirst << "), attention("
        << neediness << ")." << endl;
    }

    string getSpecies() {
      return "cat";
    }
};

class Dog : public Pet {
  private:
    // Tracks whether or not the dog needs a walk.
    int energy;

    void incEnergy() {
      int incValue = (rand() % 7);// Set to increment by no more than 7.
      energy += incValue;
    }

  public:
    // Initializes energy's value in addition to the max increment values.
    Dog(string dogName) : Pet(dogName) {
      energy = 0;
      hungerMax = 7;
      thirstMax = 4;
      needinessMax = 4;
    }

    void speak() { cout << "Bark! Bark!" << endl; }

    // Prints out needs.
    void showNeeds() {
      cout << name << " the dog needs: food(" << hunger
        << "), water(" << thirst << "), attention("
        << neediness << "), a walk(" << energy <<  ")." << endl;
    }

    // Calls the Pet class' runIncrements, then
    // increments energy.
    void runIncrements() {
      Pet::runIncrements();
      incEnergy();
    }

    // Sets energy to 0 and pays the player.
    int special(int inValue=0) {
      energy = 0;
      return 12;
    }

    string getSpecies() {
      return "dog";
    }
};

class Parrot : public Pet {
  private:
    // Likelihood the bird will extort you.
    int unscrupulousness;
 
    void incUnscrupulousness() {
      int incValue = (rand() % 8);// Set to increment by no more than 8.
      unscrupulousness += incValue;
    }
    
  public:
    // Same structure as the Dog contructor, but with
    // unscrupulousness instead of energy.
    Parrot(string parrotName) : Pet(parrotName) {
      unscrupulousness = 0;
      hungerMax = 4;
      thirstMax = 4;
      needinessMax = 6;
    }

    void speak() { cout << name << "want share of the profits." << endl; }

    // Functionally the same as previous clases.
    void showNeeds() {
      cout << name << " the parrot needs: food(" << hunger
        << "), water(" << thirst << "), attention("
        << neediness << "), your money (" << unscrupulousness << ")." << endl;
    }

    // Functionally identical to the Dog class' runIncrements().
    void runIncrements() {
      Pet::runIncrements();
      incUnscrupulousness();
    }

    // Pays the bird an amount to be specified by the player.
    // Reduces the bird's lust for cash by that amount,
    // then returns the negative of that amount so as to remove it
    // from the player's total.
    int special(int payment) {
      unscrupulousness -= payment;
      return -payment;
    }

    string getSpecies() {
      return "parrot";
    }
};

#endif
