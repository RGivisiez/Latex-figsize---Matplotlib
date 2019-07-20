def set_size(width_pt, width_fraction=1):
    """ Set the crrect figure size for a latex text. The height is chosen using the golden ratio.

    Parameters
    ----------
    width_pt: float
            Width in pts.
            
    width_fraction: float
            Fraction of the width which you wish the figure to occupy.

    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    # Width of figure
    fig_width_in_pt = width_pt * width_fraction

    # Convert from pt to inches
    inches_per_pt = 1 / 72

    # Golden ratio to set aesthetic figure height.
    # This ratio is communly used by designers.
    golden_ratio = (5.**(1/2) + 1.) / 2.

    # Figure width in inches.
    fig_width_in_inches = fig_width_in_pt * inches_per_pt
    
    # Figure height in inches.
    fig_height_in_inches = fig_width_in_inches * golden_ratio

    fig_dim = (fig_width_in_inches, fig_height_in_inches)

    return fig_dim
