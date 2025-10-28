import pytest
from selenium  import selenium

driver = webdriver.Chrome()



public class driver {
 
 
    public static void main(String[] args) {
       System.setProperty("webdriver.chrome.driver", "C:\\Usuario\\Caminho\\chromedriver.exe");
 
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
 
        driver.get("http://www.casasbahia.com.br");
 
 
 
        WebElement caixaDeBusca = driver.findElement(By.id("strBusca"));
        caixaDeBusca.sendKeys("Playstation");
        caixaDeBusca.clear();
        caixaDeBusca.sendKeys("Panela");
 
 
 
        WebElement botaoBusca = driver.findElement(By.id("btnOK"));
        botaoBusca.click();
 
 
        WebElement resultadoPesquisa = driver.findElement(By.className("nm-product-name"));
        String resultado = resultadoPesquisa.getText();
        resultado = resultado.toLowerCase();
 
        if(resultado.contains("panela") || resultado.contains("pressão") ) {
            System.out.println("Sucesso");
        } else {
            System.out.println("Erro na pesquisa");
            System.out.println("O resultado foi: " + resultado);
        }
 
 
        driver.close();
    }
 
 
 
}