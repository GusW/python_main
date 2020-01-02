'''
file        : ./postcodemixin.py
test        : ./test_ex2.py
primary     : gustavo.watanabe@gmail.com
description : Mixin class for custom mod logic - Exercise 2 helper logic
'''
from enum import Enum
import re


class PostcodeConstructor:
    def __init__(self):
        pass

    def formats(self, postcode):
        ''' Nothing to do at this level. Subclasses must implement this '''
        raise NotImplementedError()

    def validates(self, postcode):
        ''' Nothing to do at this level. Subclasses must implement this '''
        raise NotImplementedError()


class ArgentinaPostcodeConstructor(PostcodeConstructor):

    def __init__(self):
        super().__init__()

    def formats(self, postcode):
        ''' illustrative purposes only... '''
        pass

    def validates(self, postcode):
        ''' illustrative purposes only... '''
        pass


class BrazilPostcodeConstructor(PostcodeConstructor):

    def __init__(self):
        super().__init__()

    def formats(self, postcode):
        ''' illustrative purposes only... '''
        pass

    def validates(self, postcode):
        ''' illustrative purposes only... '''
        pass


class UKPostcodeConstructor(PostcodeConstructor):

    def __init__(self):
        super().__init__()
        self.special_postcodes = ('BS981TL', 'BX11LT', 'BX21LB', 'BX32BB', 'BX47SB', 'BX55AT', 'CF101BH', 'CF991NA',
                                  'CV48UW', 'CV350DB', 'DA11RT', 'DE993GG', 'DE554SW', 'DH981BT', 'DH991NS', 'E145HQ',
                                  'E145JP', 'E161XL', 'E202AQ', 'E202BB', 'E202ST', 'E203BS', 'E203EL', 'E203ET',
                                  'E203HB', 'E203HY', 'E981SN', 'E981ST', 'E981TT', 'EC2N2DB', 'EC4Y0HQ', 'EH121HQ',
                                  'EH991SP', 'G581SB', 'GIR0AA', 'IV212LR', 'L304GB', 'LS981FD', 'M502BH', 'M502QH',
                                  'N19GU', 'N811ER', 'NE14ST', 'NG801EH', 'NG801LH', 'NG801RH', 'NG801TH', 'PH15RB',
                                  'PH12SJ', 'S24SU', 'S61SW', 'S147UP', 'SA99', 'SE10NE', 'SE18UJ', 'SM60HB', 'SN381NW',
                                  'SR51SU', 'SW1A0AA', 'SW1A0PW', 'SW1A1AA', 'SW1A2AA', 'SW1A2AB', 'SW1H0TL', 'SW1P3EU',
                                  'SW1W0DT', 'SW117US', 'SW195AE', 'TW89GS', 'W1A1AA', 'W1D4FA', 'W1N4DJ', 'W1T1FB',
                                  'CO43SQ')

    def formats(self, postcode):
        ''' Returns formatted postcode '''
        postcode = self.trim_postcode(postcode)
        area, district, sector, unit = self.slice_postcode(postcode)
        return ''.join([area, district, ' ', sector, unit]).upper()

    def _validate_area(self, area):
        ''' Logic to validate postcode area info extracted from
            https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
        '''
        if len(area) <= 2:
            if area[0] not in ('Q', 'V', 'X'):
                if len(area) == 2:
                    if area[1] not in ('I', 'J', 'Z'):
                        return True
                else:
                    return True

        return False

    def _validate_district(self, area, district):
        ''' Logic to validate postcode district info extracted from
            https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
        '''
        if district[0].isdigit():
            outward = ''.join([area, district])
            if len(area) == 1:
                if area in ('B', 'E', 'G', 'L', 'M', 'N', 'S', 'W') and district.isdigit() and len(district) <= 2:
                    return True

                if not district[-1].isdigit():
                    if outward in ('E1W', 'N1C', 'N1P'):
                        return True
                    else:
                        if district[-1] in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'P', 'S', 'T', 'U', 'W'):
                            return True

            if len(area) == 2:
                if district.isdigit():
                    if int(district) == 0:
                        return True if area in ('BL', 'BS', 'CM', 'CR', 'FY', 'HA', 'PR', 'SL', 'SS') else False

                    if area in ('AB', 'LL', 'SO'):
                        return True if len(district) == 2 else False

                    elif area in ('BR', 'FY', 'HA', 'HD', 'HG', 'HR', 'HS', 'HX', 'JE', 'LD', 'SM', 'SR', 'WN', 'ZE'):
                        return True if len(district) == 1 else False

                    return True

                else:
                    if outward in ('NW1W', 'SE1P'):
                        return True

                    if (outward[:-1] in ('WC1', 'WC2', 'EC1', 'EC2', 'EC3', 'EC4', 'SW1') and
                       district[-1] in ('A', 'B', 'E', 'H', 'M', 'N', 'P', 'R', 'V', 'W', 'X', 'Y')):
                        return True

        return False

    def _validate_sector(self, sector_code):
        ''' Logic to validate postcode sector info extracted from
            https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
        '''
        return sector_code.isdigit() and len(sector_code) == 1

    def _validate_unit(self, unit_code):
        ''' Logic to validate postcode unit info extracted from
            https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
        '''
        disallowed_letters = ('C', 'I', 'K', 'M', 'O', 'V')
        return (len(unit_code) == 2 and
                not unit_code[0].isdigit() and unit_code[0] not in disallowed_letters and
                not unit_code[1].isdigit() and unit_code[1] not in disallowed_letters)

    @staticmethod
    def trim_postcode(postcode):
        ''' Remove any special char from the postcode '''
        return re.sub('[^a-zA-Z0-9\n\.]', '', str(postcode))

    @staticmethod
    def slice_postcode(postcode):
        ''' Receives a postcode string and slices information returning area, district, sector and unit info '''

        def _get_inward_code(postcode):
            ''' Three last chars of the postcode '''
            inward = postcode[-3:]
            assert len(inward) == 3, 'Inward code is not 3 chars long: %s' % len(inward)

            return inward

        def _get_outward_code(postcode):
            ''' The postcode removed the inward (3 last chars) '''
            inward = _get_inward_code(postcode)
            outward = postcode[:postcode.index(inward)]
            assert len(outward) >= 2, 'Outward code is only %s long. At least 2 expected' % len(outward)

            return outward

        def _slice_inward_code(inward_code):
            ''' The postcode removed the inward (3 last chars) '''
            return inward_code[0], inward_code[1:]

        def _slice_outward_code(outward_code):
            ''' The postcode removed the inward (3 last chars)
                District info begins with a digit
            '''
            district_idx = re.search(r"[0-9]{1}", outward_code)
            assert district_idx, 'No district reference was found in the outward code: no digits in %s' % outward_code

            return outward_code[:district_idx.start()], outward_code[district_idx.start():]

        postcode = UKPostcodeConstructor.trim_postcode(postcode)
        inward = _get_inward_code(postcode)
        outward = _get_outward_code(postcode)
        sector, unit = _slice_inward_code(inward)
        area, district = _slice_outward_code(outward)
        if all((area, district, sector, unit)):
            return area, district, sector, unit
        else:
            raise Exception('Could not slice all postcode data: area=%s, district=%s, sector=%s, unit=%s'
                            % (area, district, sector, unit))

    def validates(self, postcode):
        ''' Validate postcode given existing validation rules '''
        postcode = self.trim_postcode(postcode)
        if postcode in self.special_postcodes:
            return True
        else:
            area, district, sector, unit = self.slice_postcode(postcode)

            return all((self._validate_area(area),
                        self._validate_district(area, district),
                        self._validate_sector(sector),
                        self._validate_unit(unit)))


class PostcodeConstructorMap(Enum):
    ''' Used to map region names to its underlying postcode constructor '''
    ARG = ArgentinaPostcodeConstructor()  # Enum illustrative purposes only...
    BRA = BrazilPostcodeConstructor()     # Enum illustrative purposes only...
    UK = UKPostcodeConstructor()


class PostcodeMixin:
    ''' '''
    def _param_type_checker(self, param, param_type):
        assert isinstance(param, param_type), '%s must be %s, received %s' % (param, param_type, type(param))

    def _param_exists_checker(self, param, default):
        assert param is not None, '%s was not found!' % default

    def get_constructor_for_region(self, region):
        ''' Receives region param as str
            Returns the underlying constructor class
        '''
        self._param_type_checker(region, str)
        constructorMap = PostcodeConstructorMap.__dict__.get(region.upper())
        return constructorMap.value if constructorMap else None

    def get_action_for_constructor(self, constructor, action):
        ''' Receives constructor class and action as string
            Returns the bound action method if exists, None otherwise
        '''
        self._param_type_checker(constructor, PostcodeConstructor)
        self._param_type_checker(action, str)
        return getattr(constructor, action, None)

    def postcode_action(self, postcode, region, action):
        ''' Receives postcode, region and action as str
            Triggers the bound region's action method to the postcode
        '''
        (self._param_type_checker(postcode, str) and
         self._param_type_checker(region, str) and
         self._param_type_checker(action, str))

        postcode_constructor = self.get_constructor_for_region(region)
        self._param_exists_checker(postcode_constructor, region)

        postcode_action = self.get_action_for_constructor(postcode_constructor, action)
        self._param_exists_checker(postcode_action, action)

        return postcode_action(postcode)
