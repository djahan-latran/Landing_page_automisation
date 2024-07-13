import pandas as pd
from openai import OpenAI

class PageContent:

    def __init__(self, town_list):
        """creates PageContent instance and connects to openai api"""
        self.town_list = town_list
        api_key = open("api_key/api", "r").read()
        self.client = OpenAI(api_key=api_key)

    def _export_csv(self, csv_name):
        """helper function that exports the content file as a csv"""
        self.df.to_csv("output/" + csv_name + ".csv", index=False)

    def _create_default_df(self):
        """helper function that creates a default dataframe to fill"""
        data = {"TITLE": [None], "TEXT1": [None], "TEXT2": [None], "TEXT3": [None], "TAGS": [None]
                }
        self.df = pd.DataFrame(data)

    def _gpt_response_one(self, town_name):
        """prompts chatgpt with a specific task"""
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"Kannst du einen Text mit einer ähnlichen Struktur, ähnlichen Themen und ungefähr"
                            f" der gleichen Länge"
                            f" angepasst für {town_name} anstatt für Aachen verfassen? Bitte nutze Textabsätze nach"
                            f" Themen und nenne ortspezifische Besonderheiten oder Merkmale. "
                            f"Textreferenz: 'Aachen ist eine faszinierende Stadt im Westen Deutschlands mit einer "
                            f"Bevölkerung von etwa 250.000 Menschen."
                            f" Als historische Stadt mit einer reichen kulturellen Tradition ist Aachen bekannt für"
                            f" ihre beeindruckende Architektur,"
                            f" ihre renommierte Universität und ihre multikulturelle Atmosphäre. Die Stadt vereint "
                            f"Geschichte, Bildung und Lebensqualität auf eindrucksvolle Weise. "
                            f"Der Wohnungsbau in Aachen hat in den letzten Jahren eine dynamische Entwicklung erlebt."
                            f" Neue Wohnprojekte wurden realisiert, um dem steigenden Bedarf an Wohnraum gerecht "
                            f"zu werden."
                            f" Moderne Wohnanlagen, sorgfältig restaurierte Altbauten und zeitgemäße Neubauten bieten "
                            f"eine breite Palette an Wohnmöglichkeiten."
                            f" Besonders gefragt sind Wohnungen in zentralen Bezirken wie der Altstadt, dem "
                            f"Frankenberger Viertel und Burtscheid sowie in grünen Vororten."
                            f" Aachen ist auch ein bedeutendes Zentrum für Wissenschaft und Technologie."
                            f" Die Stadt beherbergt eine renommierte Technische Hochschule sowie zahlreiche "
                            f"Forschungsinstitute und Unternehmen"
                            f" aus verschiedenen Branchen wie Informationstechnologie, Biotechnologie und Maschinenbau."
                            f" Aachen zeichnet sich durch ihre Innovationskraft,"
                            f" ihre wirtschaftliche Dynamik und ihre international ausgerichtete "
                            f"Forschungslandschaft aus. "
                            f" Die Mietpreise für Wohnungen in Aachen variieren je nach Lage und Ausstattung. "
                            f"Im Durchschnitt liegen die Mietkosten bei etwa 11 € pro Quadratmeter."
                            f" Trotzdem bleibt Aachen aufgrund ihrer historischen Bedeutung,"
                            f" ihrer kulturellen Vielfalt und ihrer hochwertigen Lebensqualität ein attraktiver "
                            f"Wohnort für Menschen aus aller Welt."
                            f" Aachen ist eine Stadt mit einer dynamischen Entwicklung."
                            f" Der Wohnungsbau, die wirtschaftliche Stärke und die kulturelle Vielfalt prägen das "
                            f"Stadtbild und tragen zum Wachstum bei."
                            f" Die Stadt bietet eine reiche Kulturszene, eine beeindruckende Architektur und eine "
                            f"hohe Lebensqualität."
                            f" In diesem dynamischen Umfeld sind moderne Vermarktungstechniken wie 3D-Visualisierungen "
                            f"ein wichtiger Faktor,"
                            f" um potenzielle Kunden zu überzeugen und den Erfolg von Bauunternehmen und "
                            f"Projektentwicklern zu fördern.'"}
            ]
        )
        definition = response.choices[0].message.content.strip("\n").strip()

        return definition

    def _gpt_response_two(self, town_name):
        """prompts chatgpt with a specific task"""
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"Kannst du einen Text mit der gleichen Struktur, "
                            f"den gleichen Themen und ungefähr der gleichen Länge"
                            f" angepasst für {town_name} anstatt für Hamburg verfassen? "
                            f"Bitte nutze Textabsätze nach Themen. "
                            f"Textreferenz: 'Hamburg, die zweitgrößte Stadt "
                            f"Deutschlands mit über 1,8 Millionen Einwohnern, "
                            f"ist nicht nur eine pulsierende Metropole, "
                            f"sondern auch ein bedeutendes Zentrum für Architektur "
                            f"und Immobilienentwicklung. Die Stadt zeichnet sich "
                            f"durch ihre vielfältige Architektur aus, die "
                            f"von historischen Gebäuden bis hin zu modernen "
                            f"Wolkenkratzern reicht. Mit ihrer lebendigen "
                            f"Wirtschaft und ihrer wachsenden Bevölkerung "
                            f"ist Hamburg ein attraktiver Markt für "
                            f"Immobilienprojekte und städtebauliche Entwicklungen. "
                            f"In dieser dynamischen Stadt finden sich "
                            f"zahlreiche Architekturbüros, Immobilienentwickler "
                            f"und Baufirmen, die bestrebt sind, innovative "
                            f"architektonische Konzepte zu entwickeln und Immobilienprojekte "
                            f"mit überzeugenden Visualisierungen "
                            f"zu präsentieren. Hamburg bietet eine inspirierende Umgebung "
                            f"für Künstler und technologische Experten, "
                            f"um realistische und immersive 3D-Animationen von Gebäuden, "
                            f"Wohnkomplexen und städtischen "
                            f"Entwicklungen zu erstellen. Die Bedeutung von "
                            f"3D-Animationsdiensten im Bereich Architektur und "
                            f"Immobilienprojekte liegt darin, dass sie Unternehmen "
                            f"dabei unterstützen, ihre Visionen und "
                            f"Konzepte überzeugend darzustellen. Durch hochwertige "
                            f"Animationen können Unternehmen potenziellen "
                            f"Käufern und Investoren immersive Einblicke in zukünftige "
                            f"Bauprojekte bieten, ihr Interesse wecken und Vertrauen aufbauen. "
                            f"Als Dienstleister und Partner für 3D-Animationen "
                            f"im Bereich Architektur und Immobilienprojekte "
                            f"in Hamburg stehen wir Unternehmen zur Seite, "
                            f"um ihre kreativen Visionen zum Leben zu erwecken. "
                            f"Mit unserer Expertise und unserem Engagement helfen "
                            f"wir unseren Kunden, realistische "
                            f"und beeindruckende Animationen zu entwickeln, "
                            f"die ihre Projekte erfolgreich vermarkten und ihr Geschäft vorantreiben.'"}
            ]
        )
        definition = response.choices[0].message.content.strip("\n").strip()

        return definition

    def _gpt_response_three(self, town_name):
        """prompts chatgpt with a specific task"""
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"Kannst du einen Text mit der gleichen Struktur,"
                            f" den gleichen Themen und ungefähr der gleichen Länge"
                            f" angepasst für {town_name} anstatt für Hamburg "
                            f"verfassen? Bitte nutze Textabsätze nach Themen. "
                            f"Textreferenz: 'Hamburg, die zweitgrößte Stadt "
                            f"Deutschlands mit über 1,8 Millionen Einwohnern,"
                            f" ist ein bedeutendes Zentrum für Innovation und Kreativität."
                            f"Die Stadt zieht talentierte Designer und innovative "
                            f"Unternehmen aus verschiedenen Branchen an,"
                            f" die darauf abzielen, innovative Produkte zu "
                            f"entwickeln und neue Maßstäbe zu setzen."
                            f"Mit dem Hafen Hamburgs, einem der größten "
                            f"Häfen Europas, ist die Stadt ein wichtiger "
                            f"internationaler Handelsplatz und ein Knotenpunkt "
                            f"für den globalen Handel. Diese strategische"
                            f" Lage macht Hamburg zu einem idealen Standort für "
                            f"Unternehmen, die weltweit agieren und "
                            f"ihre Produkte auf internationalen Märkten positionieren "
                            f"möchten. Zusätzlich dazu ist Hamburg "
                            f"bekannt für seine vielfältige Kulturszene und sein "
                            f"reiches kulturelles Erbe. Von renommierten"
                            f" Museen und Galerien bis hin zu Theatern und Musikfestivals bietet die Stadt ein "
                            f"reichhaltiges kulturelles Angebot, das Kreativität und Innovation fördert und inspiriert."
                            f"Produktvisualisierungsdienste spielen in diesem "
                            f"dynamischen Umfeld eine entscheidende Rolle,"
                            f" indem sie Unternehmen dabei unterstützen, ihre Produkte "
                            f"ästhetisch ansprechend zu präsentieren"
                            f" und ihre Marktposition zu stärken. Als Dienstleister "
                            f"und Partner für Produktvisualisierungen"
                            f" bringen wir unsere Expertise und unser Engagement ein, "
                            f"um Unternehmen in Hamburg dabei zu unterstützen,"
                            f" ihre Produkte mit maximaler Wirkung zu präsentieren und ihr Wachstum voranzutreiben.'"}
            ]
        )
        definition = response.choices[0].message.content.strip("\n").strip()

        return definition

    def _gpt_response_four(self, town_name):
        """prompts chatgpt with a specific task"""
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"Kannst du einen Text mit der gleichen Struktur, "
                            f"den gleichen Themen und ungefähr der gleichen Länge"
                            f" angepasst für {town_name} anstatt für Hamburg verfassen? "
                            f"Bitte nutze Textabsätze nach Themen. "
                            f"Textreferenz: 'Hamburg, die zweitgrößte Stadt Deutschlands "
                            f"mit über 1,8 Millionen Einwohnern,"
                            f" bietet eine Vielzahl von potenziellen Kunden für VFX- und CGI-Dienste. "
                            f"In dieser dynamischen Stadt finden sich zahlreiche "
                            f"Werbeagenturen, Filmproduktionsstudios "
                            f"und digitale Medienagenturen. Diese Unternehmen streben danach, "
                            f"innovative visuelle Konzepte "
                            f"zu entwickeln und ihre Markenbotschaften durch "
                            f"fesselnde visuelle Effekte zu verstärken. "
                            f"Mit ihrer florierenden Filmindustrie und einer "
                            f"reichen kreativen Szene ist Hamburg ein Hotspot "
                            f"für die Entwicklung von visuellen Effekten und CGI. "
                            f"Die Stadt bietet eine inspirierende "
                            f"Umgebung für Künstler und technologische Experten, "
                            f"um neue visuelle Welten zu erschaffen und "
                            f"grenzenlose Möglichkeiten für die visuelle Gestaltung zu erkunden. "
                            f"Die Bedeutung von VFX und CGI-Diensten liegt darin, "
                            f"dass sie Unternehmen dabei unterstützen, "
                            f"ihre Produkte und Marken mit maximaler Wirkung zu präsentieren. "
                            f"Durch hochwertige visuelle "
                            f"Effekte können Unternehmen ihre Botschaften auf "
                            f"beeindruckende Weise vermitteln und das "
                            f"Interesse und die Aufmerksamkeit ihres Publikums steigern. "
                            f"Als Dienstleister und Partner für VFX und CGI "
                            f"in Hamburg stehen wir Unternehmen zur Seite, "
                            f"um ihre kreativen Visionen zum Leben zu erwecken. Mit unserer Expertise und unserem "
                            f"Engagement helfen wir unseren Kunden, innovative visuelle Lösungen zu entwickeln, "
                            f"die ihre Marke stärken und sie von der Konkurrenz abheben.'"
                 }
            ]
        )
        definition = response.choices[0].message.content.strip("\n").strip()

        return definition

    def _gpt_response_five(self, town_name):
        """prompts chatgpt with a specific task"""
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user",
                 "content": f"Kannst du einen Text mit der gleichen Struktur, "
                            f"den gleichen Themen und ungefähr der gleichen Länge"
                            f" angepasst für {town_name} anstatt für Hamburg verfassen? "
                            f"Bitte nutze Textabsätze nach Themen. "
                            f"Textreferenz: 'Hamburg, die zweitgrößte Stadt "
                            f"Deutschlands mit über 1,8 Millionen Einwohnern, "
                            f"bietet eine Vielzahl von potenziellen Kunden für "
                            f"3D-Modellierungsdienste. In dieser dynamischen "
                            f"Stadt finden sich zahlreiche Architekturbüros, "
                            f"Designagenturen, Spieleentwicklungsstudios und Produktionsfirmen. "
                            f"Diese Unternehmen streben danach, innovative "
                            f"3D-Modelle zu entwickeln, sei es für architektonische "
                            f"Entwürfe, Produktvisualisierungen, Computerspiele oder Filme. "
                            f"Mit ihrer florierenden Kreativszene "
                            f"und einem starken Fokus auf Innovation ist "
                            f"Hamburg ein idealer Standort für die Entwicklung "
                            f"hochwertiger 3D-Modelle. Die Stadt bietet eine inspirierende Umgebung für Künstler und "
                            f"technologische Experten, um neue digitale Welten "
                            f"zu erschaffen und innovative Lösungen für verschiedene Branchen zu entwickeln. "
                            f"Die Bedeutung von 3D-Modellierungsdiensten liegt darin, "
                            f"dass sie Unternehmen dabei unterstützen, "
                            f"komplexe Ideen und Konzepte in greifbare und ansprechende Modelle zu verwandeln. "
                            f"Durch hochwertige 3D-Modelle können Unternehmen "
                            f"ihre Produkte und Projekte besser visualisieren, "
                            f"ihre Designs optimieren und ihre Kunden überzeugen. "
                            f"Als Dienstleister und Partner für "
                            f"3D-Modellierung in Hamburg stehen wir Unternehmen zur Seite, um ihre kreativen Visionen "
                            f"zum Leben zu erwecken. Mit unserer Expertise "
                            f"und unserem Engagement helfen wir unseren Kunden, "
                            f"realistische und detailgetreue 3D-Modelle zu entwickeln, "
                            f"die ihre Projekte vorantreiben und ihren Erfolg fördern.'"
                 }
            ]
        )
        definition = response.choices[0].message.content.strip("\n").strip()

        return definition

    def arch_vis_content(self, csv_name_input):
        """creates the specific content for every town in the town-list, saves it as a dataframe,
        and exports it as csv file"""
        self._create_default_df()

        for town_name in self.town_list:
            town_name_caps = town_name.upper()

            definition = self._gpt_response_one(town_name=town_name)

            new_row = {"TITLE": f"Architekturvisualisierung {town_name}",
                          "TEXT1": f"ARCHITEKTURVISUALISIERUNG IN DER REGION {town_name_caps}",
                          "TEXT2": f"Wir sind URBAN 8 - 3D-Studio im Bereich fotorealistischer Visualisierung"
                                   f" für Architektur und Immobilien in der Region {town_name}.\n\n"
                                   f"Für mehr Informationen kontaktieren Sie uns telefonisch oder per Mail."
                                   f" Gerne erstellen wir Ihnen ein Angebot für Ihr Projekt.\n\n"
                                   f"Tel.: +49 (0) 157 30 12 15 08 \ninfo@urban8.de",
                          "PROMPT": f"{definition}...",
                          "TAGS": f'["Architekturvisualisierung {town_name}", "Architektur", '
                                  f'"Visualisierung", "{town_name}"]'
                       }

            self.df = self.df.append(new_row, ignore_index=True)

        self._export_csv(csv_name=csv_name_input)

    def three_d_vis_content(self, csv_name_input):
        """creates the specific content for every town in the town-list, saves it as a dataframe,
        and exports it as csv file"""
        self._create_default_df()

        for town_name in self.town_list:
            town_name_caps = town_name.upper()

            definition = self._gpt_response_one(town_name=town_name)

            new_row = {"TITLE": f"3D Visualisierung {town_name}",
                          "TEXT1": f"3D VISUALISIERUNG IN DER REGION {town_name_caps}",
                          "TEXT2": f"Wir sind URBAN 8 - 3D-Studio im Bereich fotorealistischer Visualisierung"
                                   f" für Architektur und Immobilien in der Region {town_name}.\n\n"
                                   f"Für mehr Informationen kontaktieren Sie uns telefonisch oder per Mail."
                                   f" Gerne erstellen wir Ihnen ein Angebot für Ihr Projekt.\n\n"
                                   f"Tel.: +49 (0) 157 30 12 15 08 \ninfo@urban8.de",
                          "PROMPT": f"{definition}...",
                          "TAGS": f'["3D Visualisierung {town_name}", "3D-Visualisierung", "{town_name}"]'
                       }

            self.df = self.df.append(new_row, ignore_index=True)

        self._export_csv(csv_name=csv_name_input)

    def rendering_content(self, csv_name_input):
        """creates the specific content for every town in the town-list, saves it as a dataframe,
        and exports it as csv file"""
        self._create_default_df()

        for town_name in self.town_list:
            town_name_caps = town_name.upper()

            definition = self._gpt_response_one(town_name=town_name)

            new_row = {"TITLE": f"Rendering {town_name}",
                  "TEXT1": f"RENDERINGS IN DER REGION {town_name_caps}",
                  "TEXT2": f"Wir sind URBAN 8 - 3D-Studio im Bereich fotorealistischer Renderings"
                           f" für Architektur und Immobilien in der Region {town_name}.\n\n"
                           f"Für mehr Informationen kontaktieren Sie uns telefonisch oder per Mail."
                           f" Gerne erstellen wir Ihnen ein Angebot für Ihr Projekt.\n\n"
                           f"Tel.: +49 (0) 157 30 12 15 08 \ninfo@urban8.de",
                  "PROMPT": f"{definition}..." ,
                  "TAGS": f'["Rendering {town_name}", "Rendering", "{town_name}", "3D"]'
                       }

            self.df = self.df.append(new_row, ignore_index=True)

        self._export_csv(csv_name=csv_name_input)

    def three_d_animation_content(self, csv_name_input):
        """creates the specific content for every town in the town-list, saves it as a dataframe,
        and exports it as csv file"""
        self._create_default_df()

        for town_name in self.town_list:
            town_name_caps = town_name.upper()

            definition = self._gpt_response_two(town_name=town_name)

            new_row = {"TITLE": f"3D Animation {town_name}",
                 "TEXT1": f"3D ANIMATION IN DER REGION {town_name_caps}",
                 "TEXT2": f"Wir sind URBAN 8 - Studio im Bereich 3D Animation"
                          f" für Architektur und Immobilien in der Region {town_name}.\n\n"
                          f"Für mehr Informationen kontaktieren Sie uns telefonisch oder per Mail."
                          f" Gerne erstellen wir Ihnen ein Angebot für Ihr Projekt.\n\n"
                          f"Tel.: +49 (0) 157 30 12 15 08 \ninfo@urban8.de",
                 "PROMPT": f"{definition}...",
                 "TAGS": f'["3D Animation {town_name}", "Animation", "{town_name}", "3D", "Animationsvideo"]'
                       }

            self.df = self.df.append(new_row, ignore_index=True)

        self._export_csv(csv_name=csv_name_input)

    def immo_marketing_content(self, csv_name_input):
        """creates the specific content for every town in the town-list, saves it as a dataframe,
        and exports it as csv file"""
        self._create_default_df()

        for town_name in self.town_list:
            town_name_caps = town_name.upper()

            definition = self._gpt_response(town_name=town_name)

            new_row = {"TITLE": f"Immobilienvermarktung {town_name}",
                              "TEXT1": f"VISUELLE IMMOBILIENVERMARKTUNG IN DER REGION {town_name_caps}",
                              "TEXT2": f"Wir sind URBAN 8 - Studio im Bereich visuelle Vermarktung"
                                       f" für Architektur und Immobilien in der Region {town_name}.\n\n"
                                       f"Für mehr Informationen unserer Gesamtpakete kontaktieren Sie "
                                       f"uns telefonisch oder per Mail."
                                       f" Gerne erstellen wir Ihnen ein Angebot für Ihr Projekt.\n\n"
                                       f"Tel.: +49 (0) 157 30 12 15 08 \ninfo@urban8.de",
                              "PROMPT": f"{definition}...",
                              "TAGS": f'["Immobilienvermarktung {town_name}", "Immobilie", "{town_name}",'
                                      f' "broschüre", "Rendering", "Vermarktung"]'
                       }

            self.df = self.df.append(new_row, ignore_index=True)

        self._export_csv(csv_name=csv_name_input)

    def product_vis_content(self, csv_name_input):
        """creates the specific content for every town in the town-list, saves it as a dataframe,
        and exports it as csv file"""
        self._create_default_df()

        for town_name in self.town_list:
            town_name_caps = town_name.upper()

            definition = self._gpt_response_three(town_name=town_name)

            new_row = {"TITLE": f"Produktvisualisierung {town_name}",
                 "TEXT1": f"PRODUKTVISUALISIERUNG IN DER REGION {town_name_caps}",
                 "TEXT2": f"Wir sind URBAN 8 - Studio im Bereich Produktvisualisierung und CGI"
                          f" für Projekte in der Region {town_name}.\n\n"
                          f"Für mehr Informationen kontaktieren Sie uns telefonisch oder per Mail."
                          f" Gerne erstellen wir Ihnen ein Angebot für Ihr Projekt.\n\n"
                          f"Tel.: +49 (0) 157 30 12 15 08 \ninfo@urban8.de",
                 "PROMPT": f"{definition}...",
                 "TAGS": f'["Produktvisualisierung {town_name}", "Animation", "{town_name}",'
                         f' "3D", "Produkt", "Visualisierung"]'
                       }

            self.df = self.df.append(new_row, ignore_index=True)

        self._export_csv(csv_name=csv_name_input)

    def vfx_content(self, csv_name_input):
        """creates the specific content for every town in the town-list, saves it as a dataframe,
        and exports it as csv file"""
        self._create_default_df()

        for town_name in self.town_list:
            town_name_caps = town_name.upper()

            definition = self._gpt_response_four(town_name=town_name)

            new_row = {"TITLE": f"CGI & VFX {town_name}",
                 "TEXT1": f"CGI UND VFX IN DER REGION {town_name_caps}",
                 "TEXT2": f"Wir sind URBAN 8 - Studio im Bereich CGI und VFX"
                          f" für alle Branchen in der Region {town_name}.\n\n"
                          f"Für mehr Informationen unserer Leistungen kontaktieren Sie uns telefonisch oder per Mail."
                          f" Gerne erstellen wir Ihnen ein Angebot für Ihr Projekt.\n\n"
                          f"Tel.: +49 (0) 157 30 12 15 08 \ninfo@urban8.de",
                 "TEXT3": f"{definition}...",
                 "TAGS": f'["VFX {town_name}", "CGI {town_name}", "{town_name}", "CGI", "VFX", "film effekte"]'
                       }

            self.df = self.df.append(new_row, ignore_index=True)

        self._export_csv(csv_name=csv_name_input)

    def three_d_modeling_content(self, csv_name_input):
        """creates the specific content for every town in the town-list, saves it as a dataframe,
        and exports it as csv file"""
        self._create_default_df()

        for town_name in self.town_list:
            town_name_caps = town_name.upper()

            definition = self._gpt_response_five(town_name=town_name)

            new_row = {"TITLE": f"3D Modellierung {town_name}",
                        "TEXT1": f"3D MODELLIERUNG IN DER REGION {town_name_caps}",
                        "TEXT2": f"Wir sind URBAN 8 - Studio im Bereich 3D Modellierung und CGI"
                                 f" für Projekte in der Region {town_name}.\n\n"
                                 f"Für mehr Informationen kontaktieren Sie uns telefonisch oder per Mail."
                                 f" Gerne erstellen wir Ihnen ein Angebot für Ihr Projekt.\n\n"
                                 f"Tel.: +49 (0) 157 30 12 15 08 \ninfo@urban8.de",
                        "TEXT3": f"{definition}...",
                        "TAGS": f'["3D Modellierung {town_name}", "3D", "Immobilien","{town_name}",'
                                f' "Modell", "Modellierung"]'
                       }

            self.df = self.df.append(new_row, ignore_index=True)

        self._export_csv(csv_name=csv_name_input)


