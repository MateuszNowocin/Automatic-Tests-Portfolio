package base;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Properties;

public class BaseTest {

    public static WebDriver driver;
    public static Properties properties = new Properties();
    public static FileReader fileReader;
    @BeforeTest
    public static void SetUp() throws IOException {

        if (driver == null) {
            String currentDirectory = System.getProperty("user.dir");
            System.out.println(currentDirectory);
            fileReader = new FileReader(currentDirectory + "\\src\\test\\resources\\configfiles\\configFile.properties");
            properties.load(fileReader);
        }

        if (properties.getProperty("browser").equalsIgnoreCase("chrome")) {

            WebDriverManager.chromedriver().setup();    //download the driver
            driver = new ChromeDriver();
            driver.get(properties.getProperty("testingURL"));  //get the URL from the config file

        } else if (properties.getProperty("browser").equalsIgnoreCase("firefox")) {

            WebDriverManager.firefoxdriver().setup();
            driver = new FirefoxDriver();
            driver.get(properties.getProperty("testingURL"));
        }
    }
    @AfterTest
    public void TearDown() {


    }
}
