import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;

public class Project_euler_67
{
    private static void printArrayArray(ArrayList<ArrayList<Integer>> inArrays)
    {
        for (int i = 0; i < inArrays.size(); i++)
        {
            ArrayList<Integer> currArray = inArrays.get(i);

            for (int j = 0; j < currArray.size(); j++)
                System.out.print(currArray.get(j) + " ");

            System.out.println();
        }
    }


    public static void maxTrianglePath(ArrayList<
                                ArrayList<Integer>> inTriangle)
    {
        for (int i = 0; i < inTriangle.size(); i++)
        {
            ArrayList<Integer> currArray = inTriangle.get(i);

            for (int j = 0; j < currArray.size(); j++)
            {
                int currVal = currArray.get(j);
                int highPath = currVal;
                
                try
                {
                    ArrayList<Integer> prevArray = inTriangle.get(i - 1);

                    int tmpPath;


                    try
                    {
                        tmpPath = prevArray.get(j) + currVal;

                        if (tmpPath > highPath)
                            highPath = tmpPath;
                    }
                    catch(Exception e)
                    {
                        ;
                    }

                    try
                    {
                        tmpPath = prevArray.get(j - 1) + currVal;

                        if (tmpPath > highPath)
                            highPath = tmpPath;
                    }
                    catch(Exception e)
                    {
                        ;
                    }

                    currArray.set(j, highPath);
                }
                catch(Exception e)
                {
                    ;
                }
            }
        }

        ArrayList<Integer> bottomLine = inTriangle.get(inTriangle.size() - 1);

        int high = 0;
        int currVal;
        for (int i = 0; i < bottomLine.size(); i++)
        {
            currVal = bottomLine.get(i);

            if (currVal > high)
                high = currVal;
        }

        System.out.println(high); 
    }


    public static void main(String[] args)
    {
        File inFile = new File("ex_1.in");

        try
        {
            Scanner sc = new Scanner(inFile);

            ArrayList<ArrayList<Integer>> inTriangle = 
                                            new ArrayList<ArrayList<Integer>>();

            int currNum;
            String currLine;
            while (sc.hasNextLine())
            {
                currLine = sc.nextLine();

                ArrayList<Integer> inLine = new ArrayList<Integer>();

                for (int i = 0; i < currLine.length(); i += 3)
                {
                    currNum = Integer.parseInt(currLine.substring(i, i+2));
                    inLine.add(currNum);
                }

                inTriangle.add(inLine);
            }

            maxTrianglePath(inTriangle);
        }
        catch(FileNotFoundException e)
        {
            System.out.println(e.toString());
        }
    }
}
