import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;

public class Project_euler_83
{
    static private class MatrixIndex
    {
        int val;
        boolean visited;

        MatrixIndex()
        {
            this.val = 0;
            this.visited = false;
        }

        MatrixIndex(int val)
        {
            this.val = val;
            this.visited = false;
        }
    }


    static private class Frontiersman
    {
        int x;
        int y;
        int val;

        Frontiersman()
        {
            x = -1;
            y = -1;
            val = -1;
        }


        Frontiersman(int x, int y, int val)
        {
            this.x = x;
            this.y = y;
            this.val = val;
        }
    }


    private static void printArrayArray(ArrayList<ArrayList<MatrixIndex>> inArrays)
    {
        for (int i = 0; i < inArrays.size(); i++)
        {
            ArrayList<MatrixIndex> currArray = inArrays.get(i);

            for (int j = 0; j < currArray.size(); j++)
                System.out.print(currArray.get(j).val + " ");

            System.out.println();
        }
    }


    private static void printPriorityQueue(PriorityQueue<Frontiersman>
                                                                frontier)
    {
        Frontiersman tmpFront = new Frontiersman();
        Iterator<Frontiersman> itr = frontier.iterator();

        System.out.print("[");
        while (itr.hasNext())
        {
            tmpFront = itr.next();
            System.out.print("{" + tmpFront.x + ", " + tmpFront.y + ", ");
            System.out.print(tmpFront.val + "} ");
        }
        System.out.println("]");
    }


    private static void checkFrontier(int currx, int curry, MatrixIndex currItem,
        PriorityQueue<Frontiersman> frontier, ArrayList<ArrayList<MatrixIndex>> inMatrix)
    {
        Frontiersman upFront = new Frontiersman();
        Frontiersman downFront = new Frontiersman();
        Frontiersman rightFront = new Frontiersman();
        Frontiersman leftFront = new Frontiersman();

        MatrixIndex tmpFrontIndex = new MatrixIndex();
        try
        {
            tmpFrontIndex = inMatrix.get(curry - 1).get(currx);

            if (!tmpFrontIndex.visited)
            {
                upFront.x = currx;
                upFront.y = curry - 1;
                upFront.val = currItem.val + tmpFrontIndex.val;
            }
        }
        catch (Exception e)
        {
            ;
        }
        try
        {
            tmpFrontIndex = inMatrix.get(curry).get(currx + 1);

            if (!tmpFrontIndex.visited)
            {
                rightFront.x = currx + 1;
                rightFront.y = curry;
                rightFront.val = currItem.val + tmpFrontIndex.val;
            }
        }
        catch (Exception e)
        {
            ;
        }
        try
        {
            tmpFrontIndex = inMatrix.get(curry + 1).get(currx);

            if (!tmpFrontIndex.visited)
            {
                downFront.x = currx;
                downFront.y = curry + 1;
                downFront.val = currItem.val + tmpFrontIndex.val;
            }
        }
        catch (Exception e)
        {
            ;
        }
        try
        {
            tmpFrontIndex = inMatrix.get(curry).get(currx - 1);

            if (!tmpFrontIndex.visited)
            {
                leftFront.x = currx - 1;
                leftFront.y = curry;
                leftFront.val = currItem.val + tmpFrontIndex.val;
            }
        }
        catch (Exception e)
        {
            ;
        }

        Frontiersman tmpFront = new Frontiersman();
        Iterator<Frontiersman> itr = frontier.iterator();
        while (itr.hasNext())
        {
            tmpFront = itr.next();

            if (tmpFront.y == upFront.y && tmpFront.x == upFront.x)
            {
                if (tmpFront.val > upFront.val)
                    itr.remove();
                else
                    upFront.x = -1;
            }

            if (tmpFront.y == downFront.y && tmpFront.x == downFront.x)
            {
                if (tmpFront.val > downFront.val)
                    itr.remove();
                else
                    downFront.x = -1;
            }

            if (tmpFront.y == rightFront.y && tmpFront.x == rightFront.x)
            {
                if (tmpFront.val > rightFront.val)
                    itr.remove();
                else
                    rightFront.x = -1;
            }
            if (tmpFront.y == leftFront.y && tmpFront.x == leftFront.x)
            {
                if (tmpFront.val > leftFront.val)
                    itr.remove();
                else
                    leftFront.x = -1;
            }
        }

        if (upFront.x != -1)
            frontier.add(upFront);
        if (downFront.x != -1)
            frontier.add(downFront);
        if (rightFront.x != -1)
            frontier.add(rightFront);
        if (leftFront.x != -1)
            frontier.add(leftFront);
    }


    public static void minMatrixPath(ArrayList<
                                ArrayList<MatrixIndex>> inMatrix)
    {
        // Initializing a priority queue to hold the objects that are on the
        // frontier, using their val member variables to establish weight
        PriorityQueue<Frontiersman> frontier =                            
            new PriorityQueue<Frontiersman>(10, new Comparator<Frontiersman>(){
                public int compare(Frontiersman f1, Frontiersman f2) {
                    return f1.val - f2.val;
                }     
            }    
        );

        // Initializing reuseable MatrixIndex objects
        MatrixIndex currItem = new MatrixIndex();
        MatrixIndex origItem = new MatrixIndex();
        

        // The shortest path to the top left item is itself. I account fo that
        // here.
        origItem = inMatrix.get(0).get(0);
        origItem.visited = true;
        inMatrix.get(0).set(0, origItem);

        // The current frontier becomes the items at [0, 1] and at [1, 0] so I
        // add those positions to the frontier here
        currItem = inMatrix.get(0).get(1);
        Frontiersman currFront = new Frontiersman(1, 0, (currItem.val + 
                                                        origItem.val));

        frontier.add(currFront);

        currItem = inMatrix.get(1).get(0);
        currFront.x = 0; 
        currFront.y = 1;
        currFront.val = currItem.val + origItem.val;

        frontier.add(currFront);

        // Using Dijkstra algorithm to get through the rest of it
        Frontiersman bestFrontier = frontier.poll();
        while (bestFrontier != null)
        {
            int currx = bestFrontier.x;
            int curry = bestFrontier.y;

            // First modifying and finalizing the best spot on the frontier
            currItem = inMatrix.get(curry).get(currx);
            currItem.val = bestFrontier.val;
            currItem.visited = true;
            inMatrix.get(curry).set(currx, currItem);

            // Attempting to move up, down, and to the right
            checkFrontier(currx, curry, currItem, frontier, inMatrix);

            bestFrontier = frontier.poll();            
        }

        // Grabbing the final value
        ArrayList<MatrixIndex> finalCol = inMatrix.get(inMatrix.size() - 1);
        currItem = finalCol.get(finalCol.size() - 1);

        System.out.println(currItem.val);
    }


    public static void main(String[] args)
    {
        File inFile = new File("ex_5.in");

        try
        {
            Scanner sc = new Scanner(inFile);

            ArrayList<ArrayList<MatrixIndex>> inMatrix = 
                                            new ArrayList<ArrayList<MatrixIndex>>();

            String currLine;
            while (sc.hasNextLine())
            {
                currLine = sc.nextLine();
                currLine += " ";

                ArrayList<MatrixIndex> inLine = new ArrayList<MatrixIndex>();

                int currNum;
                String numStr;
                int startLoc = 0;
                int spaceLoc;
                spaceLoc = currLine.indexOf(" ");
                while (spaceLoc != -1)
                {
                    numStr = currLine.substring(startLoc, spaceLoc);
                    currNum = Integer.parseInt(numStr);
                    MatrixIndex currIndex = new MatrixIndex(currNum);
                    inLine.add(currIndex);

                    startLoc = spaceLoc + 1;
                    spaceLoc = currLine.indexOf(" ", startLoc);
                }

                inMatrix.add(inLine);
            }

            minMatrixPath(inMatrix);
        }
        catch (FileNotFoundException e)
        {
            System.out.println(e.toString());
        }
    }
}
