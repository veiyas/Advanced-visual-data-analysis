im = im2double(imread('11.jpg'));

imHSV = rgb2hsv(im);

[H_hist, ~] = histcounts(reshape(imHSV(:,:,1), 1, size(imHSV,1)*size(imHSV,2)), [0:1/360:1]);
[S_hist, ~] = histcounts(reshape(imHSV(:,:,2), 1, size(imHSV,1)*size(imHSV,2)), [0:1/100:1]);
[V_hist, ~] = histcounts(reshape(imHSV(:,:,3), 1, size(imHSV,1)*size(imHSV,2)), [0:1/100:1]);

S1 = get_features(im)
S2 = get_features(imread('10.jpg'))

BW = edge(rgb2gray(im), 'canny');
[houghRes,T,R] = hough(BW, 'Theta', -90:0.5:89);


%%
base = get_features(imread('11.jpg'));

paths = ['0102030405060708091012'];
pathSuffix = '.jpg';
fullPath = '';

for i = 1:2:size(paths,2)
    fullPath = strcat(paths(i:i+1), pathSuffix);
    S = get_features(imread(fullPath));
end