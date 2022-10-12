/*public class Java_for_Test {
    public static int a = 5;
    //public static int b = 2;
    public static void main(String[] args)
    {
        int b = 2;
        cal(b);
        cal(b);
        System.out.println(b);
    }
    static void cal(int b)
    {
        if(b > a)
        {
            a -= 3;
        }
        else
        b += 3;
    }
}*/

public class Java_for_Test
{
    public static int[] numA = {1, 2, 3, 4, 5};
    public static void main(String[] args)
    {
        //int[] numA = {1, 2, 3, 4, 5};
        init(numA);
        prnt(numA);
    }
    static void init(int a[])
    {
        for(int i = a.length-1; i > 0; i--)
        {
            a[i] += a[i-1];
        }
    }
    static void prnt(int a[])
    {
        int sum = 0;
        for(int i : a)


        {
            sum += i;
        }
        System.out.println(sum);
    }

}