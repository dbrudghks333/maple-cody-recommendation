#!bin/bash
#
# avatar server의 /packed_character_look으로의 테스트 콜
curl -X POST -H "Content-Type: application/json" http://0.0.0.0:7000/v1/character-info -d \
"{ \
    \"user_name\": \"인품\"\
}"


# curl -X POST -H "Content-Type: application/json" http://0.0.0.0:8080/packed_character_look -d \
# "{ \
#     \"packed_character_look\": \"JMOABMIKLNNJIBGJPJFMBNOOLEHFGILCMPOJHJCENAAEAEHKDECPGEMJEMMFKLAFFPBBGGNGNLIENCMODMCEGLBCEEPOHHPCHHLJJKAANDADBMOMCBGEBFAPIKIKJDFIIDEDKJLGPLDBLBJFCCHDLDNEFCGDPANLNKKPFCAOBGJMEHMKJAHBMANPHKFBEMGODHDPFGGEKLDAJOMGNMJGPHAIDKKALGAHCLFDGDJHFFDCIJFMMFKJDABNMMEGPHLM\"\
# }"



apiVersion: v1
clusters:
- cluster:
    certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUMvakNDQWVhZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRJek1ETXdNekEyTURVeU4xb1hEVE16TURJeU9EQTJNRFV5TjFvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBTWVBCjdTQXRWMjY0U0NGcnFhcGtmQkpLaDNUdDF0OXlKdnRCMDRoQ0tLWnNQWVRFQ29PV2tVYndXN0s1RHVLS2NPQlkKZzZGbDhWSVo4UHJzNFdyL2dicW00cjhZelRWQzJ0UHlCZVkzRHJZQVVFRGlEdXRxMkZidUpBdTdwVkdDSEhlQwp0bkM0YXVzd1c5SjZFY0ZIZHozWVJBWWlhUWp3aXM1R21YbUxqeFJFMCsrRWp6M29sbFFlSkRpczREM0JvTUtkClk4aENoTzhjRldWTlhlZmRKcnJTSHUyQTRBcnYvS2NkWURSbzlDTlBpV1dYNkxXV05oUFUwcUlrdm5lRjRwdCsKZzRQR09OajJabDBKRHNRd1NkaEZkTjNlcTNJUEgrbFV4aXZvaXBROFVDNVN1Z2ZxcElSMkNkekF6QTByZUdIVgpBclJGWW91Nmk5clFVTUFVVm9FQ0F3RUFBYU5aTUZjd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0hRWURWUjBPQkJZRUZPcUdzYjFRbFVTMi9Ta01nMjZ0VXM5dTFlVk1NQlVHQTFVZEVRUU8KTUF5Q0NtdDFZbVZ5Ym1WMFpYTXdEUVlKS29aSWh2Y05BUUVMQlFBRGdnRUJBSGhPRmlNOFYzQ1BDS0xwbjdRbwprMENHMVBOTUNjODlUR1RidUlZWDllRFNEWW1OQWFvWkUzRGJVc0ExNHE1M3FUNVBDeDJXbkdWN2Q2TkI2TEpIClVJdytmTGQ4aFdHWmtOQjdqd1ArcUZZTDROcWdVMmRIYlhrSVludGZ2by9RblNRY3dqc0tOdWpha0dVRHpxRDgKWm1laHRTbjBiNTRwOWhLTXBMb1JsdmRabkxyOWRVeFRUV2ZNNllBTWtDSWY1QWlXNGN6VmZsOUJSVGkrVm02MQpOWGxiSE5ianlNTGdSRG9NUWNsYVh4VG9nemUyb0F4UVpxSnpQSk83cWkySmgrSUZZZkowbTF5c2gwSzFKZG92CnhKK1RHK2xhSGpKVWI2bUJ1LzdjSVJNTi9PNWt3Y0V3WHJCUkNoM25ueWQvQkp3aUlTeVFIbEcxSC9wQ1dFdTQKOWJBPQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==
    server: https://FED9B3733770DC9E041C1E8FB3C56806.gr7.ap-northeast-2.eks.amazonaws.com
  name: eks-demo-maple.ap-northeast-2.eksctl.io
contexts:
- context:
    cluster: eks-demo-maple.ap-northeast-2.eksctl.io
    user: i-0a5b79680d391b538@eks-demo-maple.ap-northeast-2.eksctl.io
  name: i-0a5b79680d391b538@eks-demo-maple.ap-northeast-2.eksctl.io
current-context: i-0a5b79680d391b538@eks-demo-maple.ap-northeast-2.eksctl.io
kind: Config
preferences: {}
users:
- name: i-0a5b79680d391b538@eks-demo-maple.ap-northeast-2.eksctl.io
  user:
    exec:
      apiVersion: client.authentication.k8s.io/v1alpha1
      args:
      - eks
      - get-token
      - --cluster-name
      - eks-demo-maple
      - --region
      - ap-northeast-2
      command: aws
      env:
      - name: AWS_STS_REGIONAL_ENDPOINTS
        value: regional
      provideClusterInfo: false

