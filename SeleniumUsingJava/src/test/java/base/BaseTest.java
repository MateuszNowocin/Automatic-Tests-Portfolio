package base;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Properties;

public class BaseTest {

    public static WebDriver driver;
    public static Properties properties;
    public static FileReader fileReader;
    public void SetUp() throws IOException {

        if (driver == null) {
            String currentDirectory = System.getProperty("user.dir");
            fileReader = new FileReader(currentDirectory + "SeleniumUsingJava\\src\\test\\resources\\configfiles\\configFile.properties");
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

    public void TearDown() {


    }
}
