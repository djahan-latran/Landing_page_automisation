from town_lists import TownList
from page_content import PageContent

class ProgramExecutor:

    def execute_program(self):
        """create au content pages as csv file"""

        # import and read file
        list_instance = TownList("listen/au_städte_test.txt")
        au_town_list = list_instance.create_list()

        # create page content instance
        au_page_content = PageContent(town_list=au_town_list)

        # create the desired content and export as csv file
        au_page_content.arch_vis_content(csv_name_input="au_archvis_test")
        au_page_content.three_d_vis_content(csv_name_input="au_3dvis")
        au_page_content.rendering_content(csv_name_input="au_render")
        au_page_content.three_d_animation_content(csv_name_input="au_3danim_test")
        au_page_content.immo_marketing_content(csv_name_input="au_immo_markt")
        au_page_content.product_vis_content(csv_name_input="au_productvis")
        au_page_content.vfx_content(csv_name_input="au_vfx")
        au_page_content.three_d_modeling_content(csv_name_input="au_3dmodel")


if __name__ == "__main__":
    program = ProgramExecutor()
    program.execute_program()