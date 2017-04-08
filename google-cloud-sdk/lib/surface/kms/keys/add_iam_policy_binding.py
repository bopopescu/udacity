# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Command to add IAM policy binding for a key."""

from googlecloudsdk.api_lib.cloudkms import iam
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.iam import iam_util
from googlecloudsdk.command_lib.kms import flags


class AddIamPolicyBinding(base.Command):
  r"""Add IAM policy binding to a key.

  Adds IAM policy binding to the given key.

  See https://cloud.google.com/iam/docs/managing-policies for details of
  policy role and member types.

  ## EXAMPLES
  The following command will add an IAM policy binding for the role of
  'roles/editor' for the user 'test-user@gmail.com' on the key
  `frodo` with the keyring `fellowship` and location `global`:

    $ {command} frodo \
  --keyring fellowship \
  --location global \
  --member='user:test-user@gmail.com' \
  --role='roles/editor'
  """

  # Above text based on output from function call below
  # detailed_help = iam_util.GetDetailedHelpForAddIamPolicyBinding(
  #    flags.CRYPTO_KEY_COLLECTION, 'example-crypto-key-1')

  @staticmethod
  def Args(parser):
    flags.AddCryptoKeyArgument(parser, 'whose IAM policy to modify')
    iam_util.AddArgsForAddIamPolicyBinding(parser, 'cryptokey',
                                           flags.CRYPTO_KEY_COLLECTION)

  def Run(self, args):
    crypto_key_ref = flags.ParseCryptoKeyName(args)

    return iam.AddPolicyBindingToCryptoKey(crypto_key_ref, args.member,
                                           args.role)
