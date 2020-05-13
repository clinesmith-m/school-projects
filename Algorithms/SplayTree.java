import java.util.*;

public class SplayTree <D extends Comparable<D>>
{
    class Node<D>
    {
        public D data;
        public Node<D> parent;
        public Node<D> leftChild;
        public Node<D> rightChild;

        public Node(D data)
        {
            this.data = data;
            this.parent = null;
            this.leftChild = null;
            this.rightChild = null;
        }
    }


    // Member variables for the Splay tree
    private Node<D> root;
    private int size = 0;


    public SplayTree()
    {
        root = null;
    }


    public int depthCheck(D data)
    {
        int depth = 0;

        Node<D> currNode = root;
        while (currNode != null)
        {
            depth++;

            if (currNode.data.compareTo(data) == 0)
                return depth;
            else if (currNode.data.compareTo(data) < 0)
                currNode = currNode.rightChild;
            else
                currNode = currNode.leftChild;
        }

        return -1;
    }


    private void splay(Node<D> newRoot)
    {
        if (root == newRoot)
        {
            return;
        }

        Node<D> currParent;
        Node<D> grandparent;
        while (root != newRoot)
        {
            currParent = newRoot.parent;
            grandparent = currParent.parent;

            // zig operation
            if (grandparent == null)
            {
                // Right child
                if (currParent.data.compareTo(newRoot.data) < 0)
                {
                    Node<D> b = newRoot.leftChild;

                    root = newRoot;
                    newRoot.leftChild = currParent;
                    newRoot.parent = null;
                    currParent.parent = newRoot;
                    currParent.rightChild = b;
                    if (b != null)
                        b.parent = currParent;
                }
                // Left child
                else
                {
                    Node<D> b = newRoot.rightChild;

                    root = newRoot;
                    newRoot.rightChild = currParent;
                    newRoot.parent = null;
                    currParent.parent = newRoot;
                    currParent.leftChild = b;
                    if (b != null)
                        b.parent = currParent;
                }
            }
            // zig-zig for two right children
            else if (grandparent.data.compareTo(currParent.data) < 0 &&
                     currParent.data.compareTo(newRoot.data) < 0)
            {
                Node<D> greatGrandparent = grandparent.parent;
                Node<D> b = currParent.leftChild;
                Node<D> c = newRoot.leftChild;

                newRoot.parent = greatGrandparent;
                newRoot.leftChild = currParent;
                currParent.parent = newRoot;
                currParent.leftChild = grandparent;
                currParent.rightChild = c;
                grandparent.parent = currParent;
                grandparent.rightChild = b;
                if (b != null)
                    b.parent = grandparent;
                if (c != null)
                    c.parent = currParent;
                if (greatGrandparent == null)
                    root = newRoot;
                else if (greatGrandparent.data.compareTo(grandparent.data) < 0)
                    greatGrandparent.rightChild = newRoot;
                else
                    greatGrandparent.leftChild = newRoot;
            }
            // zig-zig for two left children
            else if (grandparent.data.compareTo(currParent.data) > 0 &&
                     currParent.data.compareTo(newRoot.data) > 0)
            {
                Node<D> greatGrandparent = grandparent.parent;
                Node<D> b = newRoot.rightChild;
                Node<D> c = currParent.rightChild;

                newRoot.parent = greatGrandparent;
                newRoot.rightChild = currParent;
                currParent.parent = newRoot;
                currParent.leftChild = b;
                currParent.rightChild = grandparent;
                grandparent.parent = currParent;
                grandparent.leftChild = c;
                if (b != null)
                    b.parent = currParent;
                if (c != null)
                    c.parent = grandparent;
                if (greatGrandparent == null)
                    root = newRoot;
                else if (greatGrandparent.data.compareTo(grandparent.data) < 0)
                    greatGrandparent.rightChild = newRoot;
                else
                    greatGrandparent.leftChild = newRoot;
            }
            // zig-zag for left then right child
            else if (grandparent.data.compareTo(currParent.data) > 0 &&
                     currParent.data.compareTo(newRoot.data) < 0)
            {
                Node<D> greatGrandparent = grandparent.parent;
                Node<D> b = newRoot.leftChild;
                Node<D> c = newRoot.rightChild;

                newRoot.parent = greatGrandparent;
                newRoot.leftChild = currParent;
                newRoot.rightChild = grandparent;
                currParent.parent = newRoot;
                currParent.rightChild = b;
                grandparent.parent = newRoot;
                grandparent.leftChild = c;
                if (b != null)
                    b.parent = currParent;
                if (c != null)
                    c.parent = grandparent;
                if (greatGrandparent == null)
                    root = newRoot;
                else if (greatGrandparent.data.compareTo(grandparent.data) < 0)
                    greatGrandparent.rightChild = newRoot;
                else
                    greatGrandparent.leftChild = newRoot;
            }
            // zig-zag for right then left child
            else if (grandparent.data.compareTo(currParent.data) < 0 &&
                     currParent.data.compareTo(newRoot.data) > 0)
            {
                Node<D> greatGrandparent = grandparent.parent;
                Node<D> b = newRoot.leftChild;
                Node<D> c = newRoot.rightChild;

                newRoot.parent = greatGrandparent;
                newRoot.leftChild = grandparent;
                newRoot.rightChild = currParent;
                currParent.parent = newRoot;
                currParent.leftChild = c;
                grandparent.parent = newRoot;
                grandparent.rightChild = b;
                if (b != null)
                    b.parent = grandparent;
                if (c != null)
                    c.parent = currParent;
                if (greatGrandparent == null)
                    root = newRoot;
                else if (greatGrandparent.data.compareTo(grandparent.data) < 0)
                    greatGrandparent.rightChild = newRoot;
                else
                    greatGrandparent.leftChild = newRoot;
            }
            // Making sure I haven't messed up an if statement
            else
                System.out.println("Turns out the splay operations need work.");
        }
    }


    public boolean contains(D data)
    {
        boolean returnVal = false;

        Node<D> currNode = root;
        while (currNode != null)
        {
            if (currNode.data.compareTo(data) == 0)
            {
                returnVal = true;
                break;
            }
            else if (currNode.data.compareTo(data) < 0)
                currNode = currNode.rightChild;
            else
                currNode = currNode.leftChild;
        }

        if (returnVal)
            splay(currNode);

        return returnVal;
    }


    public void insert(D data)
    {
        if (contains(data))
            return;

        this.size++;

        Node<D> babyNode = new Node<D>(data);

        if (this.root == null)
        {
            this.root = babyNode;
            return;
        }

        Node<D> nextNode = root;
        Node<D> currNode = root;
        boolean rightChild  = false;
        while (nextNode != null)
        {
            currNode = nextNode;

            if (babyNode.data.compareTo(currNode.data) > 0)
            {
                nextNode = currNode.rightChild;
                rightChild = true;
            }
            else
            {
                nextNode = currNode.leftChild;
                rightChild = false;
            }
        }

        if (rightChild)
        {
            currNode.rightChild = babyNode;
            babyNode.parent = currNode;
        }
        else
        {
            currNode.leftChild = babyNode;
            babyNode.parent = currNode;
        }

        splay(babyNode);
    }


    public void delete(D data)
    {
        boolean foundIt = false;

        Node<D> currNode = root;
        boolean isRightChild = false;
        while (currNode != null)
        {
            if (currNode.data.compareTo(data) == 0)
            {
                foundIt = true;
                break;
            }
            else if (currNode.data.compareTo(data) < 0)
            {
                currNode = currNode.rightChild;
                isRightChild = true;
            }
            else
            {
                currNode = currNode.leftChild;
                isRightChild = false;
            }
        }

        if (foundIt)
        {
            size--;

            splay(currNode);

            // No children
            if (currNode.leftChild == null && currNode.rightChild == null)
                root = null;

            // Only right children
            else if (currNode.leftChild == null)
            {
                Node<D> replacement = currNode.rightChild;
                isRightChild = true;

                while (replacement.leftChild != null)
                {
                    replacement = replacement.leftChild;
                    isRightChild = false;
                }

                if (!isRightChild)
                {
                    currNode.rightChild.parent = replacement;
                    replacement.parent.leftChild = replacement.rightChild;
                    if (replacement.rightChild != null)
                        replacement.rightChild.parent = replacement.parent;
                    replacement.rightChild = currNode.rightChild;
                    replacement.parent = null;
                    root = replacement;
                }
                else
                {
                    replacement.parent = null;
                    root = replacement;
                }
            }
            // Only left children or left and right children
            else
            {
                Node<D> replacement = currNode.leftChild;
                isRightChild = false;

                while (replacement.rightChild != null)
                {
                    replacement = replacement.rightChild;
                    isRightChild = true;
                }

                if (isRightChild)
                {
                    if (currNode.rightChild != null)
                        currNode.rightChild.parent = replacement;
                    currNode.leftChild.parent = replacement;
                    replacement.parent.rightChild = replacement.leftChild;
                    if (replacement.leftChild != null)
                        replacement.leftChild.parent = replacement.parent;
                    replacement.leftChild = currNode.leftChild;
                    replacement.rightChild = currNode.rightChild;
                    replacement.parent = null;
                    root = replacement;
                }
                else
                {
                    replacement.rightChild = currNode.rightChild;
                    if (currNode.rightChild != null)
                        currNode.rightChild.parent = replacement;
                    replacement.parent = null;
                    root = replacement;
                }
            }
        }

    }


    public int size()
    {
        return size;
    }


    public void printTree(Node<D> currNode)
    {
        if (currNode.leftChild != null)
            printTree(currNode.leftChild);

        System.out.println(currNode.data);

        if (currNode.rightChild != null)
            printTree(currNode.rightChild);
    }


    public static void main(String[] args)
    {
        SplayTree<Integer> st = new SplayTree<Integer>();

        Random rand = new Random();
        for (int i = 0; i < 25; i++)
        {
            st.insert(rand.nextInt(100));
        }

        st.printTree(st.root);

        System.out.println();
        System.out.println("***************");
        System.out.println();

        System.out.print("Contains 25: ");
        System.out.println(st.contains(25));

        System.out.print("Contains 55: ");
        System.out.println(st.contains(55));

        System.out.print("Contains 99: ");
        System.out.println(st.contains(99));

        System.out.println();
        System.out.println("***************");
        System.out.println();

        for (int i = 20; i < 40; i++)
        {
            if (i % 2 == 0)
            {
                if (st.contains(i*2))
                    st.delete(i*2);
            }

            else if (st.contains(i))
                st.delete(i);
        }

        st.printTree(st.root);

        System.out.println();
        System.out.println("***************");
        System.out.println();

        for (int i = 0; i < 100; i++)
        {
            System.out.println("Depth: " + st.depthCheck(i));
        }

        System.out.println();
        System.out.println("***************");
        System.out.println();

        System.out.println("Size: " + st.size());

        for (int i = 0; i < 100; i++)
        {
            st.delete(i);
        }

        System.out.println("Size: " + st.size());
        System.out.println("Done.");
    }
}
