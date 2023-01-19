import java.util.Scanner;

//2. Составить алгоритм: если введенное имя совпадает с Вячеслав, то вывести “Привет, Вячеслав”,
// если нет, то вывести "Нет такого имени"
public class nameChecker {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Введите имя: ");
        String name = sc.next();
        String namecheck = "Вячеслав";
        if (name.equals(namecheck)){
            System.out.println("Привет, " + name);
        } else {
            System.out.println("Нет такого имени");
        }
        sc.close();
    }
}
