/*
 * This file is part of Libav.
 *
 * Libav is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * Libav is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with Libav; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 */


#ifndef AVUTIL_HWCONTEXT_CUDA_H
#define AVUTIL_HWCONTEXT_CUDA_H

#include <cuda.h>

#include "pixfmt.h"

/**
 * @file
 * An API-specific header for AV_HWDEVICE_TYPE_CUDA.
 *
 * This API supports dynamic frame pools. AVHWFramesContext.pool must return
 * AVBufferRefs whose data pointer is a CUdeviceptr.
 */

/**
 * This struct is allocated as AVHWDeviceContext.hwctx
 */
typedef struct AVCUDADeviceContext {
    CUcontext cuda_ctx;
} AVCUDADeviceContext;

/**
 * AVHWFramesContext.hwctx is currently not used
 */

#endif /* AVUTIL_HWCONTEXT_CUDA_H */
