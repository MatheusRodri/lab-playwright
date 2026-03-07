from playwright.sync_api import sync_playwright
import time

with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)
    contexto = navegador.new_context()

    # Abri navegador
    pagina = contexto.new_page()

    # navegar para uma pagina
    pagina.goto("https://hashtagtreinamentos.com")

    # Capturar informações da pagina
    print(pagina.title())

    #Selecionar um elemento na tela
    #1º Opção Xpath -> Não recomenda pelo playwright
    #pagina.locator('xpath=/html/body/main/section[1]/div[2]/a').click()

    #2° Opção Get -> Recomenda
    botao = pagina.locator("div").get_by_role("link", name="Quero aprender").first

    with contexto.expect_page() as pagina2_info:
        botao.click()

    #Selecionar varios elementos
    # links = pagina.locator("link").all()
    # for link in links:
    #     print(link)

    pagina2 = pagina2_info.value



    time.sleep(5)
    navegador.close()