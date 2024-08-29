#!/usr/bin/env python
# coding: utf-8

import nibabel as nib


def normalize(method,input_im, output_im):
    """Normalize/zscore MRI image"""
    nii = nib.load(input_im)
    nii_affine = nii.affine
    nii_data = nii.get_fdata()

    if method == "minmax":
        nii_data_normalized = (nii_data - nii_data.min()) / (nii_data.max() - nii_data.min())
    
    elif method == "zscore":
        nii_data_normalized = (nii_data - nii_data.mean()) / (nii_data.std())

    nib.save(nib.Nifti1Image(nii_data_normalized, affine=nii_affine), output_im)

if __name__ == "__main__":
    normalize(
        method= snakemake.params["norm_method"],
        input_im=snakemake.input["im_raw"],
        output_im=snakemake.output["im_norm"],
    )