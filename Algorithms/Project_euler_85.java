import java.util.*;

public class Project_euler_85
{
    public static void main(String[] args)
    {
        int bustNum = 2000000;

        // HashMap to hold width/number of boxes per single line pairs
        // Which just so happens to be the nth triangle number
        HashMap<Integer, Integer> triangleNums = new HashMap<Integer, Integer>(100);

        // Variables to hold best above and best below
        int bestAbove = 2147483647; // Initializing at garbage initial values
        int bestBelow = 0; // to appease the compiler
        int aboveWidth = 1, aboveLength = 1;
        int belowWidth = 1, belowLength = 1;

        // Initializing length and width variables at 1.
        int length = 1;
        int width = 1;

        // Calculating values for a rectangle with a legth of 1.
        boolean bust = false;
        int currTriNum;
        while (!bust)
        {
            currTriNum = (width * (width+1))/2;
            triangleNums.put(width, currTriNum);

            if (currTriNum < bustNum)
            {
                bestBelow = currTriNum;
                belowWidth = width;
                width++;
            }
            else
            {
                bestAbove = currTriNum;
                aboveWidth = width;
                bust = true;
            }
        }

        // Outer loop that increments length
        length++;
        while (true)
        {
            // width = length to start, so as to avoid repeated shapes
            width = length;

            // Check to see if the first iteration busts
            int triangleNum1 = triangleNums.get(length);
            int triangleNum2 = triangleNums.get(width);
            int currRectangles = triangleNum1 * triangleNum2;
            if (currRectangles > bustNum)
            {
                if (currRectangles < bestAbove)
                {
                    bestAbove = currRectangles;
                    aboveWidth = width;
                    aboveLength = length;
                }

                break;
            }

            // Inner loop that increments width until first iteration busts
            boolean innerBust = false;
            while (!innerBust)
            {
                // do the math
                triangleNum2 = triangleNums.get(width);
                currRectangles = triangleNum1 * triangleNum2;

                // If the math busts, check this number vs bestAbove and break
                if (currRectangles > bustNum)
                {
                    innerBust = true;

                    if (currRectangles < bestAbove)
                    {
                        bestAbove = currRectangles;
                        aboveWidth = width;
                        aboveLength = length;
                    }
                }

                // else, record currUnder and advance width 
                else
                {
                    if (currRectangles > bestBelow)
                    {
                        bestBelow = currRectangles;
                        belowWidth = width;
                        belowLength = length;
                    }
                }

                width++;
            }

            length++;
        } 

        // Establishing absolute values relative to the target number
        bestBelow = bustNum - bestBelow;
        bestAbove = bestAbove - bustNum;

        int bestArea;
        if (bestBelow < bestAbove)
        {
            bestArea = belowWidth*belowLength;
            System.out.println(bestArea);
        }
        else
        {
            bestArea = aboveWidth*aboveLength;
            System.out.println(bestArea);
        }
    }
}
