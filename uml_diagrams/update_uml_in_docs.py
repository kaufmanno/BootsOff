import subprocess
import os

uml_diagrams = []
s = None
with open('./uml_diagrams_in_docs.txt', 'r') as f:
    while not (s == ''):
        s = f.readline().strip('\n')
        if not (s == '' or s == ' '):
            uml_diagrams.append(s)
print(uml_diagrams)

if len(uml_diagrams) > 0:
    print('Updating UML diagrams...')
    for d in uml_diagrams:
        cmd = f'pyreverse {d} -p uml_{d}'
        print(cmd)
        out = subprocess.check_output(cmd, shell=True)
        print(out.decode('ascii'))

if len(uml_diagrams) > 0:
    print('Removing old .dot files...')
    cmd = 'rm -rf ../docs/source/uml/*.dot'
    print(cmd)
    out = subprocess.check_output(cmd, shell=True)
    print('Moving .dot files to ../docs/source...')
    print(d)
    with open('../docs/source/uml_diagrams.rst', 'w+') as rst:
        rst.write('UML diagrams\n')
        rst.write('============\n\n')
        rst.write('.. toctree::\n')
        rst.write('   :maxdepth: 1\n')
        rst.write('   :caption: Classes\n\n')

        for d in sorted(uml_diagrams):
            if os.path.exists(f'./classes_uml_{d}.dot'):
                cmd = f'mv -f -t ../docs/source/uml classes_uml_{d}.dot'
                print(cmd)
                out = subprocess.check_output(cmd, shell=True)
                print(out.decode('ascii'))
                rst.write(f'   Classes {d}<uml/classes_uml_{d}.rst>\n')
                with open(f'../docs/source/uml/classes_uml_{d}.rst', 'w+') as uml_rst:
                    title = f'Classes {d}\n'
                    uml_rst.write(title)
                    uml_rst.write('=' * len(title) + '\n\n')
                    uml_rst.write(f'.. graphviz:: classes_uml_{d}.dot')

        rst.write('\n')
        rst.write('.. toctree::\n')
        rst.write('   :maxdepth: 1\n')
        rst.write('   :caption: Packages\n\n')

        for d in sorted(uml_diagrams):
            if os.path.exists(f'./packages_uml_{d}.dot'):
                cmd = f'mv -f -t ../docs/source/uml packages_uml_{d}.dot'
                print(cmd)
                out = subprocess.check_output(cmd, shell=True)
                print(out.decode('ascii'))
                rst.write(f'   Packages {d}<uml/packages_uml_{d}.rst>\n')
                with open(f'../docs/source/uml/packages_uml_{d}.rst', 'w+') as uml_rst:
                    title = f'Packages {d}\n'
                    uml_rst.write(title)
                    uml_rst.write('=' * len(title) + '\n\n')
                    uml_rst.write(f'.. graphviz:: packages_uml_{d}.dot')


else:
    print('No files to update! Please add packages or modules whose classes are needed in docs in the '
          '"uml_diagrams_in_docs.txt" file.')
