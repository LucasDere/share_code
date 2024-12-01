from setuptools import setup

######################################################################################################
################ You May Remove All the Comments Once You Finish Modifying the Script ################
######################################################################################################

setup(

    name = 'ecolaf', 
    
    version = '0.1.0',

    description = 'A toolkit python package to build an evidential multimodal neural network for semantic segmentation or classification.',
    
    py_modules = ["ECOLAF"],

    package_dir = {'':'src'},
    
    author = 'Lucas Deregnaucourt',
    author_email = 'lucas.deregnaucourt@insa-rouen.fr',
    
    long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    long_description_content_type = "text/markdown",
    
    url='https://github.com/deregnaucourtlucas/ECOLAF',
    
    include_package_data=True,

    install_requires = [

        'torch ~= 2.0.0'

    ],
    
    keywords = ['Dempster-Shafer Theory', 'Deep Learning', 'Multimodal', 'Semantic Segmentation', 'Classification'],
    
)
