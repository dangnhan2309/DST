


text_file_types = {
    '.txt': {
        'description': 'Plain text, no formatting.',
        'use_cases': ['Notes', 'Logs', 'Code', 'Configuration']
    },
    '.rtf': {
        'description': 'Rich Text Format, supports basic text formatting.',
        'use_cases': ['Simple document formatting', 'Exchange']
    },
    '.html': {
        'description': 'HyperText Markup Language for web pages.',
        'use_cases': ['Website content', 'Webpages']
    },
    '.htm': {
        'description': 'Alternate extension for HTML files.',
        'use_cases': ['Website content', 'Webpages']
    },
    '.xml': {
        'description': 'Extensible Markup Language for structured data.',
        'use_cases': ['Data storage', 'Configuration', 'Exchange']
    },
    '.csv': {
        'description': 'Comma-Separated Values, used for tabular data.',
        'use_cases': ['Spreadsheets', 'Data export']
    },
    '.md': {
        'description': 'Markdown, lightweight markup for formatting text.',
        'use_cases': ['Documentation', 'Readme files', 'Blogs']
    },
    '.markdown': {
        'description': 'Markdown, similar to .md for text formatting.',
        'use_cases': ['Documentation', 'Readme files', 'Blogs']
    },
    '.log': {
        'description': 'Log files for tracking program activity or errors.',
        'use_cases': ['System logs', 'Application logs']
    },
    '.py': {
        'description': 'Python script file.',
        'use_cases': ['Python programming', 'Automation']
    },
    '.sh': {
        'description': 'Shell script file for UNIX/Linux systems.',
        'use_cases': ['System automation', 'Task scheduling']
    },
    '.bat': {
        'description': 'Batch file for Windows command line scripting.',
        'use_cases': ['Windows automation', 'Scripting']
    }
}
type_text_file_accepted = [
    '.docx', '.txt', '.rtf', '.html', '.htm', '.xml', 
    '.csv', '.md', '.markdown', '.log', '.py', '.sh', '.bat'
]