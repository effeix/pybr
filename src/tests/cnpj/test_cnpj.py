import pytest
from pybr import CNPJ

class TestCNPJ:
    
    # --------------------------------------------------------------------------
    # 2026 Alphanumeric standard test cases
    # Generated with https://www.gov.br/pt-br/servicos/simulador-cnpj-alfanumerico
    # --------------------------------------------------------------------------
    VALID_ALPHANUMERIC_CASES = [
        "0L.C17.MHC/0001-97", "0L.C17.MHC/LB1N-06", "13.S0T.5CG/0001-00", 
        "13.S0T.5CG/D5GM-84", "1G.6XT.4B2/0001-21", "1G.6XT.4B2/93YL-00", 
        "26.EJG.EYJ/0001-05", "26.EJG.EYJ/NV3B-60", "2L.PSN.5JP/0001-50", 
        "2L.PSN.5JP/58G9-60", "33.BCX.13A/0001-42", "33.BCX.13A/XBEG-03", 
        "3V.LJG.DD6/0001-07", "3V.LJG.DD6/6CJ3-91", "47.H1P.A3W/0001-07", 
        "47.H1P.A3W/93C3-34", "4A.LC3.76V/0001-74", "4A.LC3.76V/5400-12", 
        "6G.Z8V.YP3/0001-00", "6G.Z8V.YP3/SLWW-30", "8E.R7K.Z5V/0001-56", 
        "8E.R7K.Z5V/3595-10", "91.RPD.PZX/0001-13", "91.RPD.PZX/E36H-70", 
        "91.WVW.TC4/0001-50", "91.WVW.TC4/VPJ9-00", "9M.GMH.TTY/0001-62", 
        "9M.GMH.TTY/WJPM-69", "AH.BY0.TY7/0001-01", "AH.BY0.TY7/TSWL-35", 
        "BL.8ML.3S4/0001-50", "BL.8ML.3S4/0GYX-92", "BN.CG8.BKN/0001-29", 
        "BN.CG8.BKN/5YT8-09", "BV.PSS.8YK/0001-57", "BV.PSS.8YK/TYP8-24", 
        "C9.8P0.LWJ/0001-68", "C9.8P0.LWJ/B9N2-83", "CG.7GW.0A5/0001-30", 
        "CG.7GW.0A5/B003-87", "CW.W8V.8YB/0001-14", "CW.W8V.8YB/G165-03", 
        "EM.B7R.XKX/0001-74", "EM.B7R.XKX/0DLW-94", "G2.NZB.RMW/0001-77", 
        "G2.NZB.RMW/3H04-06", "G6.1SM.PMJ/0001-05", "G6.1SM.PMJ/ZRJ5-73", 
        "HA.P2L.YN0/0001-97", "HA.P2L.YN0/YD2K-78", "HJ.YWL.R9T/0001-26", 
        "HJ.YWL.R9T/LN2Y-80", "HT.XC6.MAX/0001-93", "HT.XC6.MAX/C295-38", 
        "J4.LKP.MJL/0001-00", "J4.LKP.MJL/EDDS-50", "L5.BN4.ATG/0001-94", 
        "L5.BN4.ATG/7JRD-50", "LG.YCT.5WB/0001-48", "LG.YCT.5WB/MSVK-41", 
        "MJ.D2M.T7V/0001-38", "MJ.D2M.T7V/RATR-93", "PD.LMM.KGW/0001-96", 
        "PD.LMM.KGW/5W85-59", "PH.0X2.RY1/0001-33", "PH.0X2.RY1/AT4A-55", 
        "PR.K35.63H/0001-69", "PR.K35.63H/SSC1-86", "S9.31X.VGK/0001-00", 
        "S9.31X.VGK/6629-00", "SP.SSK.D3M/0001-00", "SP.SSK.D3M/VTSL-24", 
        "ST.05A.D0M/0001-78", "ST.05A.D0M/9RPH-32", "TN.S7G.649/0001-10", 
        "TN.S7G.649/HWC2-79", "TP.L47.HGB/0001-96", "TP.L47.HGB/83EE-80", 
        "V5.71T.G4R/0001-43", "V5.71T.G4R/YLSP-40", "V5.7LD.8ZH/0001-81", 
        "V5.7LD.8ZH/407A-13", "WR.AYR.10N/0001-81", "WR.AYR.10N/JNT7-19", 
        "XB.H11.K36/0001-80", "XB.H11.K36/HL8N-25", "XN.TY9.0LZ/0001-46", 
        "XN.TY9.0LZ/PNDX-46", "YD.SLX.ZNB/0001-19", "YD.SLX.ZNB/AEML-03", 
        "YJ.6ST.CVD/0001-47", "YJ.6ST.CVD/BCWH-56", "ZA.CKB.7HL/0001-14", 
        "ZA.CKB.7HL/YLEC-34", "ZE.BJX.PXT/0001-45", "ZE.BJX.PXT/SD6V-91", 
        "ZJ.9PZ.4CG/0001-15", "ZJ.9PZ.4CG/YBX0-25", "ZP.VR9.3JJ/0001-31", 
        "ZP.VR9.3JJ/V6B0-18"
    ]


    # --------------------------------------------------------------------------
    # Legacy numeric standard test cases
    # Generated with https://www.4devs.com.br/gerador_de_cnpj
    # --------------------------------------------------------------------------
    VALID_LEGACY_CASES = [
        "00.441.133/0001-01", "01.020.802/0001-26", "01.074.581/0001-79",
        "01.125.615/0001-07", "01.442.746/0001-18", "03.748.652/0001-05",
        "04.536.245/0001-99", "04.571.784/0001-69", "04.600.387/0001-78",
        "05.782.665/0001-18", "05.888.801/0001-59", "06.016.476/0001-05",
        "08.514.717/0001-63", "10.006.728/0001-84", "14.524.475/0001-91",
        "16.215.507/0001-00", "16.503.512/0001-00", "17.088.527/0001-12",
        "18.018.227/0001-20", "18.330.117/0001-07", "20.800.561/0001-82",
        "22.048.607/0001-84", "22.550.567/0001-74", "23.172.260/0001-40",
        "23.733.014/0001-10", "24.418.060/0001-97", "26.354.237/0001-64",
        "27.057.403/0001-23", "27.104.457/0001-00", "30.478.013/0001-31",
        "30.875.201/0001-01", "31.326.182/0001-19", "32.452.381/0001-36",
        "32.455.680/0001-24", "32.777.608/0001-13", "35.170.485/0001-46",
        "35.838.166/0001-66", "36.535.067/0001-78", "37.217.184/0001-56",
        "37.376.533/0001-82", "38.135.067/0001-06", "38.288.633/0001-10",
        "40.161.208/0001-07", "40.810.130/0001-04", "41.113.430/0001-05",
        "42.883.715/0001-80", "44.760.121/0001-07", "45.826.177/0001-80",
        "46.277.078/0001-59", "46.815.215/0001-61", "48.332.888/0001-96",
        "48.636.865/0001-75", "48.734.746/0001-55", "48.881.212/0001-51",
        "50.447.713/0001-76", "50.666.570/0001-93", "50.777.880/0001-85",
        "51.484.585/0001-01", "53.745.423/0001-05", "53.822.806/0001-21",
        "55.753.030/0001-60", "55.843.234/0001-92", "60.740.832/0001-76",
        "60.885.677/0001-86", "61.153.331/0001-56", "61.818.256/0001-03",
        "62.766.878/0001-90", "63.264.112/0001-70", "63.340.524/0001-41",
        "63.808.340/0001-63", "65.133.261/0001-25", "65.530.253/0001-12",
        "66.347.862/0001-01", "66.575.847/0001-02", "67.183.816/0001-79",
        "67.238.068/0001-84", "67.881.333/0001-48", "70.486.475/0001-15",
        "70.832.532/0001-70", "71.180.346/0001-67", "72.874.313/0001-80",
        "73.362.351/0001-16", "73.665.506/0001-93", "74.831.082/0001-52",
        "75.247.385/0001-95", "75.852.105/0001-78", "76.145.002/0001-30",
        "76.183.668/0001-83", "76.465.467/0001-79", "77.173.445/0001-06",
        "77.812.177/0001-17", "78.773.142/0001-89", "80.560.433/0001-30",
        "80.871.556/0001-92", "82.144.104/0001-34", "84.164.343/0001-81",
        "84.441.578/0001-73", "87.405.734/0001-39", "87.502.350/0001-34",
        "88.225.672/0001-46"
    ]

    @pytest.mark.parametrize(
        "cnpj, expected",
            [
                ("0L.C17.MHC/0001-97", "0LC17MHC000197"), # Standard Strip
                ("0l.c17.mhc/0001-97", "0LC17MHC000197"), # Case Sensitivity (To Upper)
                ("0L...C17//", "0LC17"),                  # Aggressive garbage
                (None, ""),                               # Null Safety
            ]
    )
    def test_clean_leaves_digits_and_letters_only(self, cnpj, expected):
        """Ensure cleaning forces UpperCase and removes punctuation."""
        assert CNPJ.clean(cnpj) == expected

    @pytest.mark.parametrize(
        "cnpj, expected",
            [
                ("0LC17MHC000197", "0L.C17.MHC/0001-97"),
                ("0l.c17.mhc/0001-97", "0L.C17.MHC/0001-97"), # Auto-clean then format
                ("0LC17MHC0001", None),                       # Too short
                ("0LC17MHC0001970", None),                    # Too long
            ]
    )
    def test_format(self, cnpj, expected):
        """Ensure formatter applies the correct mask XX.XXX.XXX/XXXX-XX."""
        assert CNPJ.format(cnpj) == expected

    @pytest.mark.parametrize("cnpj", VALID_ALPHANUMERIC_CASES)
    def test_is_valid_2026_alphanumeric(self, cnpj):
        """
        Validates the new Alphanumeric standard.
        Note: The class must support both input formats (masked and unmasked).
        """
        assert CNPJ.is_valid(cnpj) is True

    @pytest.mark.parametrize("cnpj", VALID_ALPHANUMERIC_CASES)
    def test_is_valid_2026_alphanumeric_unformatted(self, cnpj):
        """
        Validates the new Alphanumeric standard.
        Note: The class must support both input formats (masked and unmasked).
        """
        clean = cnpj.replace(".", "").replace("/", "").replace("-", "")
        
        assert CNPJ.is_valid(clean) is True

    @pytest.mark.parametrize("cnpj", VALID_LEGACY_CASES)
    def test_is_valid_legacy_numeric(self, cnpj):
        """Ensure backward compatibility with standard numeric CNPJs."""
        assert CNPJ.is_valid(cnpj) is True

    @pytest.mark.parametrize("cnpj", VALID_LEGACY_CASES)
    def test_is_valid_legacy_numeric_unformatted(self, cnpj):
        """Ensure backward compatibility with standard numeric CNPJs."""
        clean = cnpj.replace(".", "").replace("/", "").replace("-", "")
        
        assert CNPJ.is_valid(clean) is True

    @pytest.mark.parametrize(
        "cnpj",
            [
                "13.S0T.5CG/0001-01",  # Almost valid, wrong last digit
                "AA.AAA.AAA/AAAA-AA",  # Check digits (last 2) MUST be numeric
                "11.111.111/1111-11",  # Repeated sequence (Guard check)
                "22.222.222/2222-22",  # Repeated sequence
                "0L.C17.MHC/0001",     # Too short
                "0L.C17.MHC/0001-979", # Too long
                "",                    # Empty
                None,                  # None type
            ]
    )
    def test_is_valid_failures(self, cnpj):
        """Tests that should fail logic or checksums."""
        assert CNPJ.is_valid(cnpj) is False

    def test_validate_raises_error(self):
        """Ensure validate() raises ValueError on bad inputs."""
        with pytest.raises(ValueError) as excinfo:
            CNPJ.validate("0L.C17.MHC/0001-00") # Deliberately wrong checksum
        
        assert "Invalid CNPJ" in str(excinfo.value)
