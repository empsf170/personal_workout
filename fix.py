import os
import glob

workspace = r'c:\Users\DELL\Downloads\FORGEFIT_ACTIVE_MENU_TEXT_FIXED_GitHub'
html_files = glob.glob(os.path.join(workspace, '*.html'))

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Navbar top space
    content = content.replace('top:14px;left:50%;', 'top:0;left:50%;')
    
    # 2. Scroll top keep bottom right corner
    content = content.replace('margin:4px auto 11px;cursor:pointer}', 'position:fixed;bottom:20px;right:20px;z-index:1000;cursor:pointer;box-shadow:0 4px 12px rgba(0,0,0,0.15)}')
    
    # 3. Mob view hero section button same size
    content = content.replace('@media(max-width:560px){', '@media(max-width:560px){.actions .btn{width:100%;margin-bottom:10px;}')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print('Done!')
