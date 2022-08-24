'''
FilePath: main.py
Author: LiRunze
Date: 2022-08-23 20:31:51
LastEditors: LiRunze
LastEditTime: 2022-08-23 20:42:46
Description: 
'''

import configs
from game import Game2048

def main(args):
    '''
    screen_width: Width of the form
    screen_height: Height of the form
    block_gap: Gap between two blocks
    block_size: Size of a block
    '''
    width   = args.screen_width
    height  = args.screen_height
    gap     = args.block_gap
    size    = args.block_size
    arc     = args.block_arc

    g = Game2048(width, height, gap, size, arc)
    g.Form()

if __name__ == '__main__':
    args = configs.parse_args()
    main(args)
