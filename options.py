import argparse

class TrainOptions():
  def __init__(self):
    self.parser = argparse.ArgumentParser()

    # data loader relateds
    self.parser.add_argument('--train_dataroot', type=str, default='./dataset/train/', help='path of train datasets')
    self.parser.add_argument('--test_dataroot', type=str, default='./dataset/test/',help='path of test datasets')
    self.parser.add_argument('--dataset', type=str, default='RoadScene', help='dataset:RoadScene or PET-MRI')
    self.parser.add_argument('--phase', type=str, default='train', help='phase for dataloading')
    self.parser.add_argument('--batch_size', type=int, default=2, help='batch size')
    self.parser.add_argument('--nThreads', type=int, default=16, help='threads for data loader')
    
    # ouptput related
    self.parser.add_argument('--display_dir', type=str, default='./logs', help='path for saving display results')
    self.parser.add_argument('--img_dir', type=str, default='reg', help='path for saving result images and models')
    self.parser.add_argument('--model_dir', type=str, default='weight',help='path for saving result images and models')
    self.parser.add_argument('--display_freq', type=int, default=50, help='freq (iteration) of display')
    self.parser.add_argument('--img_save_freq', type=int, default=50, help='freq (epoch) of saving images')
    self.parser.add_argument('--model_save_freq', type=int, default=50, help='freq (epoch) of saving models')
    self.parser.add_argument('--no_display_img', action='store_true', help='specified if no dispaly')

    # training related
    self.parser.add_argument('--lr_policy', type=str, default='lambda', help='type of learn rate decay')
    self.parser.add_argument('--n_ep_Fu', type=int, default=150, help='epochs of training Encoder & Decoder')  # 400 * d_iter

    self.parser.add_argument('--n_ep', type=int, default=4500, help='number of epochs') # 400 * d_iter
    self.parser.add_argument('--n_ep_decay', type=int, default=2500, help='epoch start decay learning rate, set -1 if no decay') # 200 * d_iter
    self.parser.add_argument('--resume', type=str, default=None, help='specified the dir of saved models for resume the training')
    self.parser.add_argument('--gpu', type=int, default=0, help='gpu')
    
    self.parser.add_argument('--dataroot_val', type=str, default='./dataset/test/MSRS/', help="data for segmentation validation")

  def parse(self):
    self.opt = self.parser.parse_args()
    # args = vars(self.opt)
    # print('\n--- load options ---')
    # for name, value in sorted(args.items()):
    #   print('%s: %s' % (str(name), str(value)))
    return self.opt
