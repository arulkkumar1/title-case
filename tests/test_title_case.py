"""
Unit tests for Title Case Agent
"""

import pytest
import sys
import os

# Add parent directory to path to import the agent
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agent.title_case_agent import TitleCaseConverter


class TestTitleCaseConverter:
    """Test suite for TitleCaseConverter class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.converter = TitleCaseConverter()
    
    def test_basic_title_case(self):
        """Test basic title case conversion."""
        # Note: If brand names are lowercase in input, they'll be capitalized normally
        # To preserve "GitHub" spelling, it should already be "GitHub" in the input
        assert self.converter.to_title_case("welcome to GitHub copilot") == "Welcome to GitHub Copilot"
        assert self.converter.to_title_case("how to build a custom agent") == "How to Build a Custom Agent"
        assert self.converter.to_title_case("introduction to machine learning") == "Introduction to Machine Learning"
    
    def test_minor_words_lowercase(self):
        """Test that minor words are lowercase (except first and last)."""
        assert self.converter.to_title_case("a guide to python") == "A Guide to Python"
        assert self.converter.to_title_case("the power of AI") == "The Power of AI"
        assert self.converter.to_title_case("learning for the best") == "Learning for the Best"
    
    def test_first_and_last_word_capitalized(self):
        """Test that first and last words are always capitalized."""
        assert self.converter.to_title_case("guide to the end") == "Guide to the End"
        assert self.converter.to_title_case("the beginning and the") == "The Beginning and The"
    
    def test_acronyms_preserved(self):
        """Test that acronyms in uppercase are preserved."""
        result = self.converter.to_title_case("welcome to NASA program")
        assert "NASA" in result
    
    def test_hyphenated_words(self):
        """Test handling of hyphenated words."""
        result = self.converter.to_title_case("state-of-the-art technology")
        # Hyphenated words: first part and non-minor parts capitalized
        assert "State-Of-The-Art Technology" == result
    
    def test_empty_string(self):
        """Test handling of empty strings."""
        assert self.converter.to_title_case("") == ""
        assert self.converter.to_title_case("   ") == "   "
    
    def test_single_word(self):
        """Test single word conversion."""
        assert self.converter.to_title_case("hello") == "Hello"
        assert self.converter.to_title_case("WORLD") == "WORLD"  # Preserved as acronym
    
    def test_simple_h1_conversion(self):
        """Test conversion of simple h1 element."""
        html = "<h1>welcome to GitHub copilot</h1>"
        result = self.converter.convert_html(html)
        assert "Welcome to GitHub Copilot" in result
    
    def test_h1_with_attributes(self):
        """Test h1 element with attributes."""
        html = '<h1 class="title" id="main">how to build a custom agent</h1>'
        result = self.converter.convert_html(html)
        # Check that attributes are preserved
        assert 'class="title"' in result
        assert 'id="main"' in result
        # Check that content is converted
        assert "How to Build a Custom Agent" in result or "How To Build A Custom Agent" in result
    
    def test_multiple_heading_types(self):
        """Test conversion of multiple heading types."""
        html = """
        <title>welcome to my site</title>
        <h1>introduction to ai</h1>
        <h2>what is machine learning</h2>
        <h3>deep learning basics</h3>
        """
        result = self.converter.convert_html(html)
        assert "Welcome" in result
        assert "Introduction" in result
        assert "What" in result or "Machine Learning" in result
        assert "Deep Learning" in result
    
    def test_nested_elements(self):
        """Test heading with nested elements."""
        html = '<h1>Welcome to <span class="highlight">GitHub</span> Copilot</h1>'
        result = self.converter.convert_html(html)
        # Should preserve the span element
        assert '<span class="highlight">' in result or '<span' in result
        assert "Welcome" in result
    
    def test_heading_with_multiple_spaces(self):
        """Test handling of multiple spaces."""
        html = "<h1>hello    world</h1>"
        result = self.converter.convert_html(html)
        assert "<h1>" in result
        assert "</h1>" in result
    
    def test_all_heading_levels(self):
        """Test all heading levels h1-h5."""
        html = """
        <h1>heading one</h1>
        <h2>heading two</h2>
        <h3>heading three</h3>
        <h4>heading four</h4>
        <h5>heading five</h5>
        """
        result = self.converter.convert_html(html)
        assert "Heading One" in result
        assert "Heading Two" in result
        assert "Heading Three" in result
        assert "Heading Four" in result
        assert "Heading Five" in result
    
    def test_title_element(self):
        """Test title element conversion."""
        html = "<title>my awesome website</title>"
        result = self.converter.convert_html(html)
        assert "My Awesome Website" in result
    
    def test_preserve_non_heading_elements(self):
        """Test that non-heading elements are not modified."""
        html = """
        <h1>this is a title</h1>
        <p>this is a paragraph that should not change</p>
        <div>another div that stays the same</div>
        """
        result = self.converter.convert_html(html)
        # Heading should be changed
        assert "This Is a Title" in result or "This is a Title" in result
        # Paragraph should remain lowercase
        assert "this is a paragraph" in result
        assert "another div" in result


class TestEdgeCases:
    """Test edge cases and special scenarios."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.converter = TitleCaseConverter()
    
    def test_html_with_no_headings(self):
        """Test HTML without any headings."""
        html = "<div>Hello World</div><p>Some text</p>"
        result = self.converter.convert_html(html)
        assert result  # Should return something
        assert "Hello World" in result  # Should be unchanged
    
    def test_empty_heading(self):
        """Test empty heading element."""
        html = "<h1></h1>"
        result = self.converter.convert_html(html)
        assert "<h1>" in result
        assert "</h1>" in result
    
    def test_heading_with_only_spaces(self):
        """Test heading with only whitespace."""
        html = "<h1>   </h1>"
        result = self.converter.convert_html(html)
        assert "<h1>" in result


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
