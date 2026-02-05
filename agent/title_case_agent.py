"""
Title Case Agent for GitHub Copilot
Converts HTML heading elements (title, h1-h5) to title case while preserving attributes and sub-elements.
"""

from bs4 import BeautifulSoup
import re
from typing import List


class TitleCaseConverter:
    """Converts HTML heading text to title case."""
    
    # Minor words that should typically be lowercase in title case
    MINOR_WORDS = {
        'a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'in', 'nor',
        'of', 'on', 'or', 'so', 'the', 'to', 'up', 'yet', 'from'
    }
    
    def __init__(self):
        self.heading_tags = ['title', 'h1', 'h2', 'h3', 'h4', 'h5']
    
    def to_title_case(self, text: str) -> str:
        """
        Convert text to title case following standard rules.
        
        Rules:
        - Capitalize the first word and last word
        - Capitalize all major words (not in MINOR_WORDS)
        - Keep minor words lowercase unless they're first or last
        - Preserve acronyms and proper nouns where possible
        
        Args:
            text: The text to convert
            
        Returns:
            Text converted to title case
        """
        if not text or not text.strip():
            return text
        
        words = text.split()
        result = []
        
        for i, word in enumerate(words):
            # Check if word is all uppercase (likely an acronym like AI, NASA, HTML)
            if word.isupper() and len(word) >= 2:
                result.append(word)
                continue
            
            # Check if word contains uppercase letters in the middle (like GitHub, iPhone)
            # Preserve mixed case proper nouns
            if any(c.isupper() for c in word[1:]) and not word.isupper():
                # This is likely a proper noun with specific capitalization
                result.append(word)
                continue
            
            # Split on hyphens to handle hyphenated words
            if '-' in word:
                parts = word.split('-')
                capitalized_parts = []
                for j, part in enumerate(parts):
                    # Preserve all-caps parts in hyphenated words
                    if part.isupper() and len(part) >= 2:
                        capitalized_parts.append(part)
                    # First/last word of sentence, or first part of hyphenated word
                    elif i == 0 or i == len(words) - 1 or j == 0:
                        capitalized_parts.append(part.capitalize())
                    # Minor words in the middle of hyphenated phrases
                    elif part.lower() in self.MINOR_WORDS:
                        capitalized_parts.append(part.lower())
                    # Major words
                    else:
                        capitalized_parts.append(part.capitalize())
                result.append('-'.join(capitalized_parts))
            else:
                # First word or last word should always be capitalized
                if i == 0 or i == len(words) - 1:
                    result.append(word.capitalize())
                # Minor words should be lowercase (unless first/last)
                elif word.lower() in self.MINOR_WORDS:
                    result.append(word.lower())
                # Major words should be capitalized
                else:
                    result.append(word.capitalize())
        
        return ' '.join(result)
    
    def process_heading_element(self, element):
        """
        Process a heading element, converting its direct text content to title case.
        Preserves attributes and nested elements.
        
        Args:
            element: BeautifulSoup element to process
        """
        # Process only the direct text content, not nested elements
        if element.string:
            # Simple case: element has only text content
            element.string.replace_with(self.to_title_case(element.string))
        else:
            # Complex case: element has mixed content (text + nested elements)
            for content in element.contents:
                if isinstance(content, str):
                    # Convert text nodes to title case
                    content.replace_with(self.to_title_case(content))
                # Leave nested elements as-is (they'll be processed recursively if needed)
    
    def convert_html(self, html_content: str) -> str:
        """
        Convert all heading elements in HTML to title case.
        
        Args:
            html_content: HTML string to process
            
        Returns:
            Modified HTML with title-cased headings
        """
        # Parse HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find and process all heading elements
        for tag_name in self.heading_tags:
            for element in soup.find_all(tag_name):
                self.process_heading_element(element)
        
        # Return modified HTML
        return str(soup)
    
    def convert_html_file(self, input_file: str, output_file: str = None) -> None:
        """
        Convert heading elements in an HTML file to title case.
        
        Args:
            input_file: Path to input HTML file
            output_file: Path to output HTML file (if None, overwrites input)
        """
        # Read input file
        with open(input_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Convert headings
        converted_html = self.convert_html(html_content)
        
        # Write output file
        output_path = output_file if output_file else input_file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(converted_html)


def main():
    """Main entry point for the agent."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python title_case_agent.py <input_file> [output_file]")
        print("If output_file is not specified, input file will be modified in place.")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    converter = TitleCaseConverter()
    
    try:
        converter.convert_html_file(input_file, output_file)
        print(f"Successfully converted headings in {input_file}")
        if output_file:
            print(f"Output written to {output_file}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
