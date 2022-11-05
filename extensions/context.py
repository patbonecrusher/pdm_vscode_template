import datetime
import os


from copier_templates_extensions import ContextHook

class ContextUpdater(ContextHook):
    update = False

    def hook(self, context):
        if context['python'] == 'asdf':
            context['asdf_dir'] = os.getenv('ASDF_DIR')

        if context['python_version'] is not None:
            revs=context['python_version'].split('.')
            context['python_major_version'] = f'{revs[0]}.{revs[1]}'


        # if context['license'] != 'None':
        #     context['creation_year'] = datetime.date.today().strftime("%Y")

        # context['has_main'] = 'executable' in context['project_type']
        return context