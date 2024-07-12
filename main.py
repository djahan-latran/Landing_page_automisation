from town_lists import TownList
from page_content import PageContent

class ProgramExecutor:

    def execute_program(self):

        # create au content pages as csv file
        list_instance = TownList("listen/au_städte.txt")
        au_town_list = list_instance.create_list()
        au_page_content = PageContent(town_list=au_town_list)

        au_page_content.arch_vis_content()
        au_page_content.export_csv(csv_name="au_arch_vis")

        au_page_content.three_d_vis_content()
        au_page_content.export_csv(csv_name="au_3d_vis")

        au_page_content.rendering_content()
        au_page_content.export_csv(csv_name="au_render")

        au_page_content.three_d_animation_content()
        au_page_content.export_csv(csv_name="au_3d_anim")

        au_page_content.immo_marketing_content()
        au_page_content.export_csv(csv_name="au_immo")

        au_page_content.product_vis_content()
        au_page_content.export_csv(csv_name="au_pro_vis")

        au_page_content.vfx_content()
        au_page_content.export_csv(csv_name="au_vfx")

        au_page_content.three_d_modeling_content()
        au_page_content.export_csv(csv_name="au_3d_model")

if __name__ == "__main__":
    program = ProgramExecutor()
    program.execute_program()