from aqt.reviewer import Reviewer
from anki.hooks import wrap

def hide_expected_interval(self, i, v3_labels, _old):
    """
    Get the original button time HTML but make the text invisible
    while preserving the original structure and spacing.
    
    Args:
        self: The Reviewer instance
        i: The button index
        v3_labels: Whether using V3 scheduler labels
        _old: The original _buttonTime function
    
    Returns:
        Modified HTML that preserves layout but hides text content
    """
    # Call the original function to get the proper HTML structure
    original_html = _old(self, i, v3_labels)
    
    # If there's no content, just return as is
    if not original_html or original_html == "<div class=spacer></div>":
        return original_html
    
    # Wrap the original HTML in a span that makes the text transparent
    # but preserves all the spacing and structure
    return f"<span style='color:transparent'>{original_html}</span>"

# Patch the Reviewer._buttonTime method to hide the interval text
Reviewer._buttonTime = wrap(Reviewer._buttonTime, hide_expected_interval, "around") 