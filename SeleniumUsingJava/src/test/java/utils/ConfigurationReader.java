package utils;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Properties;

public class ConfigurationReader {
    private FileReader fileReader;
    private Properties properties;

    public ConfigurationReader() {
        try {
            fileReader = new FileReader("C:\\Repos\\Automatic-Tests-Portfolio\\SeleniumUsingJava\\src\\test\\resources\\configfiles\\configFile.properties");
            properties = new Properties();
            properties.load(fileReader);
        } catch (FileNotFoundException e) {
            throw new RuntimeException("Configuration file not found", e);
        } catch (IOException e) {
            throw new RuntimeException("Failed to load properties from the configuration file", e);
        } finally {
            try {
                if (fileReader != null) {
                    fileReader.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
