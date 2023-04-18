import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scr = new Scanner(System.in);

        int arr [] = new int[10];

        for (int i = 0; i < arr.length; i++) {
            arr[i] = scr.nextInt()%42;

        }
        int count=0;
        int total=0;
        for (int i = 0; i < arr.length; i++) {
            for (int j = i+1; j < 10; j++) {
                if (arr[i]==arr[j] && arr[i]>=0) {
                    count++;
                    arr[j]=-1;
                }
                total=10-count;
            }}
            System.out.println(total);
    }
}
