from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
    
    TEST_DATE = datetime.today().strftime('%Y-%m-%d')
    WIDTH = 210
    HEIGHT = 297

    def create_title(self, day:str, title:str = "Weekly Report"):
        # Unicode is not yet supported in the py3k version; use windows-1252 standard font
        self.set_font('Arial', '', 24)  
        self.ln(60)
        self.write(5, f"Weekly Report")
        self.ln(10)
        self.set_font('Arial', '', 16)
        self.write(4, f'{day}')
        self.ln(5)
        
    def set_page_text_style(self,):
        # Line break
        self.ln(20)
        self.set_font('Arial', '', 14)
        
    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 6)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')
        
    def first_page(self, 
                   page_1_txt1:str,
                   page_1_txt2:str,
                   page_1_img_path:str)->None:
        
        self.add_page()
        self.create_title(self.TEST_DATE)
        self.set_page_text_style()
        self.cell(30, 10, page_1_txt1, ln = 0, align='L')
        # Move to 16 cm to the right
        self.cell(155)
        self.cell(10, 10, page_1_txt2, align='R', ln = 1,)
        # Line break
        self.ln(30)
        self.image(page_1_img_path, 5, 140, self.WIDTH-20)
        
    def second_page(self, 
                    page_2_text:str,
                    page_2_img_path1:str,
                    page_2_img_path2:str,
                    page_2_img_path3:str)->None:
        
        self.add_page()        
        self.set_page_text_style()
        self.cell(0, 10, page_2_text, 0, 0, 'C')
        self.image(page_2_img_path1, 5, 60, self.WIDTH/2-10)
        self.image(page_2_img_path2, self.WIDTH/2, 60, self.WIDTH/2.1-10)
        self.image(page_2_img_path3, self.WIDTH/4, 160, self.WIDTH/2-10)
        
    def third_page(self,
                   page_3_text,
                   page_3_img_path1:str,
                   page_3_img_path2:str)->None:
        
        self.add_page()        
        self.set_page_text_style()
        self.cell(0, 10, page_3_text, 0, 0, 'C')
        self.image(page_3_img_path1, 50, 60, self.WIDTH/1.65-20)
        self.image(page_3_img_path2, 40, 170, self.WIDTH/1.35-20)
        
    def create_analytics_report(self,
                                page_1_txt1:str='Average orders per week: ~66.',
                                page_1_txt2:str='Average Revenue per order: ~480',
                                page_2_text:str="Most Desirable Product: 'D' ~21 orders",
                                page_3_text:str="Most Proactive Provider: 'Roadrunner' ~22 orders",
                                page_1_img_path:str="./plots/trend.png",
                                page_2_img_path1:str="./plots/top_products_revenue.png",
                                page_2_img_path2:str="./plots/top_products.png",
                                page_2_img_path3:str="./plots/product_sales_trend.png",
                                page_3_img_path1:str="./plots/top_providers.png",
                                page_3_img_path2:str="./plots/provider_revenue_trend.png",
                                save_filename="report.pdf"):

        pdf = FPDF() # A4 (210 by 297 mm)


        ''' First Page '''
        self.first_page(page_1_txt1,
                        page_1_txt2,
                        page_1_img_path)
        
        ''' Second Page '''
        self.second_page(page_2_text,
                         page_2_img_path1,
                         page_2_img_path2,
                         page_2_img_path3)

        
        ''' Third Page '''
        self.third_page(page_3_text,
                        page_3_img_path1,
                        page_3_img_path2)

        self.output(save_filename, 'F')

        print('Report Succesfully generated!')