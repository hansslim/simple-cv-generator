import os
import re
import json
import sys

def run_tests():
    print("=" * 60)
    print(" Spouštím testovací sadu pro Simple CV Generator")
    print("=" * 60)
    
    passed = 0
    failed = 0

    def assert_test(name, condition, error_msg=""):
        nonlocal passed, failed
        if condition:
            print(f" [PASS] {name}")
            passed += 1
        else:
            print(f" [FAIL] {name}: {error_msg}")
            failed += 1

    base_dir = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(base_dir, "index.html")
    cv_json_path = os.path.join(base_dir, "cv.json")
    robots_path = os.path.join(base_dir, "robots.txt")
    sitemap_path = os.path.join(base_dir, "sitemap.xml")

    # TEST 1: Soubory existují
    assert_test("1.1 Existence souboru index.html", os.path.isfile(index_path))
    assert_test("1.2 Existence ukázkového souboru cv.json", os.path.isfile(cv_json_path))
    assert_test("1.3 Existence souboru robots.txt", os.path.isfile(robots_path))
    assert_test("1.4 Existence souboru sitemap.xml", os.path.isfile(sitemap_path))

    with open(index_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # TEST 2: Validita cv.json
    try:
        with open(cv_json_path, "r", encoding="utf-8") as f:
            cv_data = json.load(f)
        assert_test("2.1 Validita formátu cv.json", isinstance(cv_data, dict))
        assert_test("2.2 Přítomnost klíče personal v cv.json", "personal" in cv_data)
        assert_test("2.3 Přítomnost klíče experience v cv.json", "experience" in cv_data)
        assert_test("2.4 Přítomnost klíče education v cv.json", "education" in cv_data)
    except Exception as e:
        assert_test("2.1 Validita cv.json", False, str(e))

    # TEST 3: SEO a Meta tagy
    assert_test("3.1 Přítomnost meta viewport", '<meta name="viewport"' in html_content)
    assert_test("3.2 Přítomnost meta description", '<meta name="description"' in html_content)
    assert_test("3.3 Přítomnost canonical linku", '<link rel="canonical"' in html_content)
    assert_test("3.4 Přítomnost Schema.org JSON-LD", 'application/ld+json' in html_content)
    assert_test("3.5 Přítomnost Open Graph meta tagů", 'property="og:title"' in html_content)

    # TEST 4: UI a Branding
    assert_test("4.1 Název aplikace Simple CV Generator", 'Simple CV Generator' in html_content)
    assert_test("4.2 Přítomnost tlačítka Tisk do PDF", 'Tisk do PDF' in html_content)
    assert_test("4.3 Přítomnost tlačítka Export JSON", 'Export JSON' in html_content)
    assert_test("4.4 Přítomnost tlačítka Import JSON", 'Import JSON' in html_content)
    assert_test("4.5 Přítomnost odkazu na GitHub", 'https://github.com/hansslim/simple-cv-generator' in html_content)

    # TEST 5: Vue logika a metody v setup()
    required_setup_methods = [
        "cv", "expandedSections", "isCollapsed", "toggleCollapse", 
        "showAboutModal", "isItemFilled", "renderedPages", "changeScale", 
        "resetScale", "triggerPrint", "exportJson", "triggerImport", "handleImport"
    ]
    for method in required_setup_methods:
        assert_test(f"5. Přítomnost '{method}' v setup()", re.search(r'\b' + method + r'\b', html_content) is not None)

    # TEST 6: Sbalení sekcí (Collapse / Expand)
    assert_test("6.1 Výchozí sbalení v isCollapsed", "const isCollapsed = (key) => !expandedSections.value[key];" in html_content)
    assert_test("6.2 Přítomnost třídy is-collapsed v šabloně", ":class=\"{ 'is-collapsed': isCollapsed(" in html_content)

    # TEST 7: Chytré skrývání prázdných položek
    assert_test("7.1 Logika isItemFilled pro filtrování prázdných položek", "const isItemFilled = (type, item) => {" in html_content)

    # TEST 8: CSS pro tisk (@media print)
    assert_test("8.1 Přítomnost @media print pravidel", "@media print {" in html_content)
    assert_test("8.2 Skrytí ovládacích panelů při tisku", ".editor-pane," in html_content and "display: none !important;" in html_content)
    assert_test("8.3 Nastavení rozměrů A4 297mm", "297mm" in html_content)

    print("-" * 60)
    print(f" Výsledek testů: {passed} prošlo, {failed} selhalo")
    print("=" * 60)

    if failed > 0:
        sys.exit(1)

if __name__ == "__main__":
    run_tests()
